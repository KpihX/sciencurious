#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess
import json

# Define the segments and their text scripts in French
ACTS = {
    "prologue": (
        "Bienvenue dans l'odyssée de l'intégration. Bernhard Riemann a imaginé "
        "l'aire sous une courbe par des rectangles. Mais ce modèle s'effondre avec "
        "des fonctions sauvages comme celle de Dirichlet, qui vaut un sur les rationnels "
        "et zéro sur les irrationnels. Peu importe la finesse des rectangles, la somme "
        "supérieure vaut toujours un et la somme inférieure vaut zéro. Riemann ne peut pas trancher."
    ),
    "lebesgue": (
        "En 1902, Henri Lebesgue propose une nouvelle perspective : découper l'axe "
        "des ordonnées au lieu de l'axe des abscisses. Il somme des hauteurs fixes pondérées "
        "par la mesure de leurs antécédents. Avec cette théorie de la mesure, la fonction de "
        "Dirichlet trouve enfin une valeur d'intégration : elle vaut zéro. Mais Lebesgue exige "
        "une absolue intégrabilité. Des fonctions semi-convergentes comme le sinus cardinal "
        "divergent sous son test."
    ),
    "stieltjes": (
        "Thomas Stieltjes élargit l'outil en intégrant par rapport à une fonction g(x). "
        "En probabilités, cela unifie les variables discrètes et continues sous une formule "
        "unique pour l'espérance mathématique, où la fonction de répartition dicte la mesure locale."
    ),
    "kurzweil": (
        "Kurzweil et Henstock réintroduisent Riemann avec une jauge locale delta(x) pour "
        "adapter les rectangles. Ce modèle dompte Dirichlet, intègre le sinus cardinal, "
        "et donne une version parfaite du théorème fondamental du calcul. Mais son espace "
        "fonctionnel n'est pas complet, perdant les espaces Lp de Lebesgue. Il n'existe pas "
        "d'intégration parfaite, chaque outil est un compromis."
    )
}

# edge-tts resolved from PATH (uv project env provides it — `uv add edge-tts`).
# Override with EDGE_TTS_PATH env var if a specific binary is needed.
EDGE_TTS_PATH = os.environ.get("EDGE_TTS_PATH") or shutil.which("edge-tts") or "edge-tts"

def get_audio_duration(file_path):
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", file_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return float(res.stdout.strip())

def main():
    print("--> 1. Generating audio clips using edge-tts...")
    durations = {}
    audio_files = []
    
    import time
    for act_name, script_text in ACTS.items():
        audio_filename = f"{act_name}.mp3"
        print(f"   Generating {audio_filename}...")
        
        cmd = [
            EDGE_TTS_PATH, "--voice", "fr-FR-HenriNeural",
            "--text", script_text, "--write-media", audio_filename
        ]
        
        # Retry logic for network robust synthesis
        max_retries = 5
        for attempt in range(max_retries):
            try:
                subprocess.run(cmd, check=True, capture_output=True)
                break
            except subprocess.CalledProcessError as exc:
                if attempt == max_retries - 1:
                    print(f"Error generating voice after {max_retries} attempts: {exc.stderr.decode()}", file=sys.stderr)
                    raise
                print(f"      [Retry {attempt+1}/{max_retries}] 503 Handshake Error. Waiting 3s...")
                time.sleep(3.0)
        
        # Get duration
        dur = get_audio_duration(audio_filename)
        # Add 1.5 seconds cushion to ensure text transitions smoothly
        durations[act_name] = dur + 1.5
        audio_files.append(audio_filename)
        print(f"   {act_name} duration: {durations[act_name]:.2f}s")

    # Write durations to JSON for Manim
    with open("durations.json", "w") as f:
        json.dump(durations, f, indent=4)
    print("--> 2. Wrote durations.json successfully.")

    # Concat audio clips using ffmpeg concat demuxer
    print("--> 3. Merging audio clips...")
    with open("concat_list.txt", "w") as f:
        for audio_file in audio_files:
            f.write(f"file '{audio_file}'\n")
            
    cmd_merge = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", "concat_list.txt", "-c", "copy", "narration.mp3"
    ]
    subprocess.run(cmd_merge, check=True, capture_output=True)
    print("   Created narration.mp3 successfully.")

    # Compile manim video
    print("--> 4. Running Manim Community compiler...")
    # Use -qh for high quality, --media_dir .tmp_media to avoid pollution
    cmd_manim = [
        "manim", "-qh", "--media_dir", ".tmp_media",
        "scene.py", "RiemannVsLebesgue"
    ]
    subprocess.run(cmd_manim, check=True)
    
    # Path of generated video
    manim_video = ".tmp_media/videos/scene/1080p60/RiemannVsLebesgue.mp4"
    if not os.path.exists(manim_video):
        print(f"Error: manim video not found at {manim_video}", file=sys.stderr)
        sys.exit(1)
    
    # Stitch video and audio
    print("--> 5. Stitching video and narration with ffmpeg...")
    final_output = "../assets/integration.mp4"
    cmd_stitch = [
        "ffmpeg", "-y", "-i", manim_video, "-i", "narration.mp3",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-shortest", final_output
    ]
    subprocess.run(cmd_stitch, check=True, capture_output=True)
    print(f"--> SUCCESS: Generated stitched video: {final_output}")

    # Cleanup temp files
    print("--> 6. Cleaning up temporary files...")
    temp_files = audio_files + ["concat_list.txt", "durations.json", "narration.mp3"]
    for temp_file in temp_files:
        if os.path.exists(temp_file):
            os.remove(temp_file)
    subprocess.run(["rm", "-rf", ".tmp_media"], check=True)
    print("   Cleanup done. Finished successfully!")

if __name__ == "__main__":
    main()

from manim import *
import numpy as np
import json
import os

class RiemannVsLebesgue(Scene):
    def construct(self):
        # Load custom segment durations if they exist
        durations = {
            "prologue": 15.0,
            "lebesgue": 20.0,
            "stieltjes": 15.0,
            "kurzweil": 20.0
        }
        if os.path.exists("durations.json"):
            try:
                with open("durations.json", "r") as f:
                    durations.update(json.load(f))
            except Exception:
                pass

        # ----------------------------------------------------
        # ACT I: Prologue & Riemann Limitations (durations["prologue"])
        # ----------------------------------------------------
        title = Text("L'Odyssée de l'Intégration", font_size=40, color=BLUE_C).to_edge(UP)
        self.play(Write(title))
        
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 4, 1],
            axis_config={"color": GREY_B},
            x_length=9,
            y_length=5,
        ).shift(0.5 * DOWN)
        
        def f(x):
            return 3.0 - 0.5 * (x - 3.5)**2
            
        curve = axes.plot(f, x_range=[1.0, 6.0], color=YELLOW)
        curve_label = MathTex("f(x)", color=YELLOW, font_size=28).next_to(curve, UR, buff=0.1)
        
        self.play(Create(axes), Create(curve), Write(curve_label))
        
        riemann_title = Text("Riemann : Découpage du Domaine (Axe X)", font_size=28, color=ORANGE).to_edge(DOWN).shift(0.2 * UP)
        riemann_formula = MathTex(
            r"\int_a^b f(x) \, dx \approx \sum_i f(x_i) \, \Delta x_i", 
            font_size=32, 
            color=ORANGE
        ).next_to(title, DOWN, buff=0.2)
        
        self.play(Write(riemann_title), Write(riemann_formula))
        
        rects_coarse = axes.get_riemann_rectangles(
            curve, x_range=[1.0, 6.0], dx=1.0, input_sample_type="left",
            fill_opacity=0.3, stroke_width=1.5, stroke_color=ORANGE
        )
        self.play(Create(rects_coarse))
        
        rects_fine = axes.get_riemann_rectangles(
            curve, x_range=[1.0, 6.0], dx=0.2, input_sample_type="left",
            fill_opacity=0.4, stroke_width=0.5, stroke_color=ORANGE
        )
        self.play(Transform(rects_coarse, rects_fine))
        
        # Dirichlet Function text overlay
        dirichlet_box = VGroup(
            Text("Fonction de Dirichlet D(x) :", font_size=24, color=RED),
            MathTex(r"D(x) = 1 \text{ si } x \in \mathbb{Q}", font_size=24, color=RED),
            MathTex(r"D(x) = 0 \text{ si } x \notin \mathbb{Q}", font_size=24, color=RED),
            Text("Riemann : Somme supérieure = 1, inférieure = 0 -> Indécidable", font_size=20, color=RED_C)
        ).arrange(DOWN, center=True).to_edge(LEFT).shift(UP * 0.5)
        
        self.play(FadeIn(dirichlet_box))
        
        # Wait remainder of ACT I
        act1_spent = 5.0 # approximate animation time
        self.wait(max(1.0, durations["prologue"] - act1_spent))
        
        # Clean up ACT I
        self.play(
            FadeOut(rects_coarse), FadeOut(riemann_title), FadeOut(riemann_formula),
            FadeOut(dirichlet_box)
        )

        # ----------------------------------------------------
        # ACT II: Lebesgue Slicing & sin(x)/x (durations["lebesgue"])
        # ----------------------------------------------------
        lebesgue_title = Text("Lebesgue : Découpage de l'Image (Axe Y)", font_size=28, color=TEAL_C).to_edge(DOWN).shift(0.2 * UP)
        lebesgue_formula = MathTex(
            r"\int_a^b f(x) \, dx \approx \sum_j y_j \, \mu(E_j)", 
            font_size=32, 
            color=TEAL_C
        ).next_to(title, DOWN, buff=0.2)
        
        self.play(Write(lebesgue_title), Write(lebesgue_formula))
        
        def get_lebesgue_slabs(num_slabs):
            slabs = VGroup()
            y_max = 3.0
            dy = y_max / num_slabs
            for j in range(num_slabs):
                yj = j * dy
                half_width = np.sqrt(2.0 * (3.0 - yj))
                x_start = 3.5 - half_width
                x_end = 3.5 + half_width
                p_bottom_left = axes.coords_to_point(x_start, yj)
                p_top_right = axes.coords_to_point(x_end, yj + dy)
                
                rect = Rectangle(
                    width=p_top_right[0] - p_bottom_left[0],
                    height=p_top_right[1] - p_bottom_left[1],
                    fill_color=TEAL_D, fill_opacity=0.35,
                    stroke_color=TEAL_C, stroke_width=1.0
                ).move_to((p_bottom_left + p_top_right) / 2.0)
                slabs.add(rect)
            return slabs
            
        slabs_coarse = get_lebesgue_slabs(6)
        self.play(Create(slabs_coarse))
        slabs_fine = get_lebesgue_slabs(20)
        self.play(Transform(slabs_coarse, slabs_fine))
        
        # Display Lebesgue Dirichlet solution
        dirichlet_sol = MathTex(
            r"\int_0^1 D(x) \, dx = 1 \cdot \mu(\mathbb{Q}) + 0 \cdot \mu(\mathbb{R} \setminus \mathbb{Q}) = 0", 
            font_size=24, color=TEAL_D
        ).to_edge(LEFT).shift(UP * 0.5)
        self.play(FadeIn(dirichlet_sol))
        
        # Wait remainder of Lebesgue explanation
        act2_spent = 6.0
        self.wait(max(1.0, durations["lebesgue"] - act2_spent))
                # Clean up ACT II
        self.play(
            FadeOut(slabs_coarse), FadeOut(lebesgue_title), FadeOut(lebesgue_formula),
            FadeOut(dirichlet_sol), FadeOut(curve), FadeOut(curve_label), FadeOut(axes),
            FadeOut(title)
        )
        # ACT III: Lebesgue-Stieltjes & Probability (durations["stieltjes"])
        # ----------------------------------------------------
        ls_title = Text("Lebesgue-Stieltjes : Mesures Personnalisées", font_size=28, color=PURPLE_C).to_edge(UP)
        ls_formula = MathTex(
            r"\int_a^b f(x) \, dg(x)", 
            font_size=42, 
            color=PURPLE
        ).move_to(2 * UP)
        
        prob_title = Text("Unification en Probabilités", font_size=24, color=WHITE).move_to(0.5 * UP)
        prob_formula = MathTex(
            r"\mathbb{E}[f(X)] = \int_{-\infty}^{\infty} f(x) \, dF(x)", 
            font_size=36, 
            color=YELLOW_C
        ).move_to(0.5 * DOWN)
        
        self.play(Write(ls_title), Write(ls_formula))
        self.play(Write(prob_title), Write(prob_formula))
        
        # Draw small graphic showing step function (discrete CDF) vs smooth function (continuous CDF)
        cdf_axes = Axes(
            x_range=[-2, 2, 1], y_range=[0, 1, 0.5],
            axis_config={"color": GREY_C}, x_length=4, y_length=2
        ).to_edge(DOWN).shift(0.2 * UP)
        
        continuous_cdf = cdf_axes.plot(lambda x: 1 / (1 + np.exp(-3*x)), color=BLUE)
        self.play(Create(cdf_axes), Create(continuous_cdf))
        
        act3_spent = 5.0
        self.wait(max(1.0, durations["stieltjes"] - act3_spent))
        
        self.play(
            FadeOut(ls_title), FadeOut(ls_formula), FadeOut(prob_title),
            FadeOut(prob_formula), FadeOut(cdf_axes), FadeOut(continuous_cdf)
        )

        # ----------------------------------------------------
        # ACT IV: Kurzweil-Henstock & Conclusion (durations["kurzweil"])
        # ----------------------------------------------------
        kh_title = Text("Kurzweil-Henstock : Le Triomphe de la Jauge", font_size=28, color=RED_D).to_edge(UP)
        kh_formula = MathTex(
            r"\forall x, \, |t_i - x_i| < \delta(t_i)", 
            font_size=32, 
            color=RED_C
        ).next_to(kh_title, DOWN, buff=0.2)
        
        self.play(Write(kh_title), Write(kh_formula))
        
        comparison = Table(
            [
                ["Riemann", "Intuitif / Simple", "Fonctions sauvages"],
                ["Lebesgue", "Espaces complets L^p", "Semi-convergence"],
                ["Kurzweil-Henstock", "Théorème fondamental", "Non complet"]
            ],
            col_labels=[Text("Théorie", color=YELLOW), Text("Force", color=GREEN), Text("Faiblesse", color=RED)],
            include_outer_lines=True
        ).scale(0.7).shift(DOWN * 0.8)
        
        self.play(Create(comparison))
        
        act4_spent = 6.0
        self.wait(max(1.0, durations["kurzweil"] - act4_spent))
        
        self.play(FadeOut(kh_title), FadeOut(kh_formula), FadeOut(comparison))
        
        # Epilogue
        final_text = Text("Il n'existe pas d'intégration parfaite. Chaque outil est un compromis.", font_size=24, color=BLUE_C)
        self.play(Write(final_text))
        self.wait(3.0)
        self.play(FadeOut(final_text))

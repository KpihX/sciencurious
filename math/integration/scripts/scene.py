from manim import *
import numpy as np
import json
import os

class RiemannVsLebesgue(Scene):
    def construct(self):
        # Load custom segment durations if they exist
        durations = {
            "prologue": 25.0,
            "lebesgue": 30.0,
            "stieltjes": 20.0,
            "kurzweil": 25.0
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
        title = Text("L'Odyssée de l'Intégration", font_size=36, color=BLUE_B).to_edge(UP)
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
        
        riemann_title = Text("Riemann : Découpage du Domaine (Axe X)", font_size=26, color=ORANGE).to_edge(DOWN).shift(0.2 * UP)
        riemann_formula = MathTex(
            r"\int_a^b f(x) \, dx \approx \sum_i f(x_i) \, \Delta x_i", 
            font_size=28, 
            color=ORANGE
        ).next_to(title, DOWN, buff=0.1)
        
        self.play(Write(riemann_title), Write(riemann_formula))
        
        # Continuous animation of Riemann rectangles using ValueTracker
        dx_tracker = ValueTracker(1.5)
        rects = always_redraw(lambda: axes.get_riemann_rectangles(
            curve, x_range=[1.0, 6.0], dx=dx_tracker.get_value(),
            input_sample_type="left", fill_opacity=0.35,
            stroke_width=1.0, stroke_color=ORANGE
        ))
        
        self.add(rects)
        self.play(dx_tracker.animate.set_value(0.06), run_time=8.0, rate_func=linear)
        self.wait(1.0)
        
        # Fade out Riemann elements to introduce Dirichlet
        self.play(FadeOut(rects), FadeOut(riemann_title), FadeOut(riemann_formula))
        
        # Dirichlet visual concept
        dirichlet_title = Text("Le Peigne de Dirichlet D(x)", font_size=24, color=RED).next_to(title, DOWN, buff=0.1)
        self.play(Write(dirichlet_title))
        
        # Create Dirichlet points clouds
        dots_q = VGroup()
        dots_ir = VGroup()
        np.random.seed(42)
        for _ in range(120):
            xq = np.random.uniform(1.0, 6.0)
            xir = np.random.uniform(1.0, 6.0)
            dots_q.add(Dot(axes.coords_to_point(xq, 2.5), radius=0.03, color=RED))
            dots_ir.add(Dot(axes.coords_to_point(xir, 0.5), radius=0.03, color=BLUE_B))
            
        line_q = Line(axes.coords_to_point(1.0, 2.5), axes.coords_to_point(6.0, 2.5), color=RED, stroke_width=1)
        line_ir = Line(axes.coords_to_point(1.0, 0.5), axes.coords_to_point(6.0, 0.5), color=BLUE_B, stroke_width=1)
        lbl_q = MathTex("D(x) = 1 \\text{ (Rationnels)}", font_size=20, color=RED).next_to(line_q, LEFT)
        lbl_ir = MathTex("D(x) = 0 \\text{ (Irrationnels)}", font_size=20, color=BLUE_B).next_to(line_ir, LEFT)
        
        self.play(Create(line_q), Create(line_ir), Write(lbl_q), Write(lbl_ir))
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.5) for d in dots_q], lag_ratio=0.01),
            LaggedStart(*[FadeIn(d, scale=0.5) for d in dots_ir], lag_ratio=0.01),
            run_time=3.5
        )
        
        # Fluctuation animation representing Riemann's indecision
        rects_opt = axes.get_riemann_rectangles(curve, x_range=[1.0, 6.0], dx=0.5, input_sample_type="right", fill_opacity=0.2, stroke_color=RED)
        rects_pess = axes.get_riemann_rectangles(curve, x_range=[1.0, 6.0], dx=0.5, input_sample_type="left", fill_opacity=0.2, stroke_color=BLUE_B)
        
        for _ in range(2):
            self.play(FadeIn(rects_opt), run_time=0.4)
            self.play(ReplacementTransform(rects_opt, rects_pess), run_time=0.4)
            self.play(FadeOut(rects_pess), run_time=0.4)
            
        act1_spent = 19.6 # Total approximate time spent in Act I animations
        self.wait(max(1.0, durations["prologue"] - act1_spent))
        
        self.play(
            FadeOut(line_q), FadeOut(line_ir), FadeOut(lbl_q), FadeOut(lbl_ir),
            FadeOut(dots_q), FadeOut(dots_ir), FadeOut(dirichlet_title)
        )

        # ----------------------------------------------------
        # ACT II: Lebesgue Slicing & sin(x)/x (durations["lebesgue"])
        # ----------------------------------------------------
        lebesgue_title = Text("Lebesgue : Découpage de l'Image (Axe Y)", font_size=26, color=TEAL_C).to_edge(DOWN).shift(0.2 * UP)
        lebesgue_formula = MathTex(
            r"\int_a^b f(x) \, dx \approx \sum_j y_j \, \mu(E_j)", 
            font_size=28, 
            color=TEAL_C
        ).next_to(title, DOWN, buff=0.1)
        
        self.play(Write(lebesgue_title), Write(lebesgue_formula))
        
        # Helper to generate Lebesgue horizontal slabs
        def get_lebesgue_slabs(num_slabs):
            slabs = VGroup()
            if num_slabs < 2:
                return slabs
            y_max = 3.0
            dy = y_max / num_slabs
            for j in range(num_slabs):
                yj = j * dy
                val = 3.0 - yj
                # Prevent negative sqrt due to float precision
                half_width = np.sqrt(2.0 * max(0.0, val))
                x_start = 3.5 - half_width
                x_end = 3.5 + half_width
                p_bottom_left = axes.coords_to_point(x_start, yj)
                p_top_right = axes.coords_to_point(x_end, yj + dy)
                
                rect = Rectangle(
                    width=max(0.01, p_top_right[0] - p_bottom_left[0]),
                    height=max(0.01, p_top_right[1] - p_bottom_left[1]),
                    fill_color=TEAL_D, fill_opacity=0.35,
                    stroke_color=TEAL_C, stroke_width=0.8
                ).move_to((p_bottom_left + p_top_right) / 2.0)
                slabs.add(rect)
            return slabs
            
        # Continuous animation of Lebesgue slabs
        slabs_tracker = ValueTracker(2)
        slabs = always_redraw(lambda: get_lebesgue_slabs(int(slabs_tracker.get_value())))
        self.add(slabs)
        self.play(slabs_tracker.animate.set_value(28), run_time=8.0, rate_func=linear)
        self.wait(1.0)
        
        # Show Dirichlet Lebesgue solution
        dirichlet_sol = MathTex(
            r"\int_0^1 D(x) \, d\mu = 1 \cdot \mu(\mathbb{Q}) + 0 \cdot \mu(\mathbb{R}\setminus\mathbb{Q}) = 0", 
            font_size=24, color=TEAL_B
        ).to_edge(LEFT).shift(UP * 0.5)
        self.play(FadeIn(dirichlet_sol))
        self.wait(2.0)
        
        # Transition to sin(x)/x graph
        self.play(
            FadeOut(slabs), FadeOut(lebesgue_title), FadeOut(lebesgue_formula),
            FadeOut(dirichlet_sol), FadeOut(curve), FadeOut(curve_label), FadeOut(axes)
        )
        
        # New axes for sin(x)/x
        s_axes = Axes(
            x_range=[0, 15, 2], y_range=[-0.5, 1.1, 0.5],
            axis_config={"color": GREY_C}, x_length=9, y_length=4.5
        ).shift(0.5 * DOWN)
        
        def sinc(x):
            if x == 0:
                return 1.0
            return np.sin(x) / x
            
        sinc_curve = s_axes.plot(sinc, x_range=[0.1, 14.5], color=YELLOW)
        sinc_label = MathTex(r"f(x) = \frac{\sin x}{x}", color=YELLOW, font_size=26).next_to(sinc_curve, UR, buff=0.1)
        
        self.play(Create(s_axes), Create(sinc_curve), Write(sinc_label))
        
        # Draw alternating positive/negative arches
        arches = VGroup()
        for i in range(4):
            x_start = max(0.1, i * np.pi)
            x_end = (i + 1) * np.pi
            color = GREEN if i % 2 == 0 else RED
            opacity = 0.3
            arch = s_axes.get_area(sinc_curve, x_range=[x_start, x_end], color=color, opacity=opacity)
            arches.add(arch)
            
        self.play(Create(arches), run_time=4.0)
        
        act2_spent = 17.5
        self.wait(max(1.0, durations["lebesgue"] - act2_spent))
        
        self.play(
            FadeOut(s_axes), FadeOut(sinc_curve), FadeOut(sinc_label),
            FadeOut(arches), FadeOut(title)
        )

        # ----------------------------------------------------
        # ACT III: Lebesgue-Stieltjes & Probability (durations["stieltjes"])
        # ----------------------------------------------------
        ls_title = Text("Lebesgue-Stieltjes : Mesures Personnalisées", font_size=26, color=PURPLE_B).to_edge(UP)
        ls_formula = MathTex(
            r"\int_a^b f(x) \, dg(x)", 
            font_size=38, 
            color=PURPLE
        ).move_to(2 * UP)
        
        prob_title = Text("Unification des Probabilités", font_size=22, color=WHITE).move_to(0.6 * UP)
        prob_formula = MathTex(
            r"\mathbb{E}[f(X)] = \int_{-\infty}^{\infty} f(x) \, dF(x)", 
            font_size=32, 
            color=YELLOW_B
        ).move_to(0.3 * DOWN)
        
        self.play(Write(ls_title), Write(ls_formula))
        self.play(Write(prob_title), Write(prob_formula))
        
        # Display smooth vs step CDF graphs with scanning line
        cdf_axes = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[0, 1, 0.5],
            axis_config={"color": GREY_C}, x_length=4.5, y_length=2.2
        ).to_edge(DOWN).shift(0.1 * UP)
        
        continuous_cdf = cdf_axes.plot(lambda x: 1 / (1 + np.exp(-2.5*x)), color=BLUE)
        self.play(Create(cdf_axes), Create(continuous_cdf))
        
        # Scanning vertical line showing weight concentration
        scan_line = Line(cdf_axes.coords_to_point(-2, 0), cdf_axes.coords_to_point(-2, 1.2), color=YELLOW, stroke_width=2.0)
        self.play(Create(scan_line))
        self.play(scan_line.animate.move_to(cdf_axes.coords_to_point(2, 0)), run_time=5.0, rate_func=linear)
        
        act3_spent = 9.5
        self.wait(max(1.0, durations["stieltjes"] - act3_spent))
        
        self.play(
            FadeOut(ls_title), FadeOut(ls_formula), FadeOut(prob_title),
            FadeOut(prob_formula), FadeOut(cdf_axes), FadeOut(continuous_cdf),
            FadeOut(scan_line)
        )

        # ----------------------------------------------------
        # ACT IV: Kurzweil-Henstock & Conclusion (durations["kurzweil"])
        # ----------------------------------------------------
        kh_title = Text("Kurzweil-Henstock : Le Triomphe de la Jauge", font_size=26, color=RED_C).to_edge(UP)
        kh_formula = MathTex(
            r"|t_i - x_i| < \delta(t_i) \quad \text{(Jauge locale adaptative)}", 
            font_size=28, 
            color=RED_B
        ).next_to(kh_title, DOWN, buff=0.1)
        
        self.play(Write(kh_title), Write(kh_formula))
        
        # Table comparing Riemann, Lebesgue and Kurzweil-Henstock
        comparison = Table(
            [
                ["Riemann", "Intuitif / Simple", "Fonctions sauvages"],
                ["Lebesgue", "Espaces complets L^p", "Semi-convergence"],
                ["Kurzweil-Henstock", "Théorème fondamental", "Non complet"]
            ],
            col_labels=[Text("Théorie", color=YELLOW), Text("Force", color=GREEN), Text("Faiblesse", color=RED)],
            include_outer_lines=True
        ).scale(0.65).shift(DOWN * 0.8)
        
        self.play(Create(comparison))
        
        # Animating the highlight of the Kurzweil-Henstock row to draw eyes dynamically
        kh_row_highlight = Rectangle(
            width=comparison.get_width() + 0.2, height=0.6,
            fill_color=RED_A, fill_opacity=0.2, stroke_color=RED_C, stroke_width=1.5
        ).move_to(comparison.get_rows()[3])
        
        self.play(Create(kh_row_highlight), run_time=3.0)
        
        act4_spent = 5.5
        self.wait(max(1.0, durations["kurzweil"] - act4_spent))
        
        self.play(FadeOut(kh_title), FadeOut(kh_formula), FadeOut(comparison), FadeOut(kh_row_highlight))
        
        # Epilogue
        final_text = Text("Il n'existe pas d'intégration parfaite. Chaque outil est un compromis.", font_size=24, color=BLUE_C)
        self.play(Write(final_text))
        self.wait(3.5)
        self.play(FadeOut(final_text))

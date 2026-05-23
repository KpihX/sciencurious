from manim import *
import numpy as np


class RiemannVsLebesgue(Scene):
    def construct(self):
        # 1. Title & Introduction
        title = Text("Riemann vs. Lebesgue Integration", font_size=40, color=BLUE_C).to_edge(UP)
        self.play(Write(title))
        
        # 2. Define the axes and function
        # We use a simple symmetric single-peaked function: f(x) = 3 - 0.5 * (x - 3.5)^2
        # Defined on the domain [1.0, 6.0]
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
        self.wait(1.0)
        
        # 3. Riemann Partition (x-axis slicing)
        riemann_title = Text("Riemann: Slicing the Domain (X-Axis)", font_size=28, color=ORANGE).to_edge(DOWN).shift(0.2 * UP)
        riemann_formula = MathTex(
            r"\int_a^b f(x) \, dx \approx \sum_i f(x_i) \, \Delta x_i", 
            font_size=32, 
            color=ORANGE
        ).next_to(title, DOWN, buff=0.2)
        
        self.play(Write(riemann_title), Write(riemann_formula))
        
        # Draw Riemann rectangles with coarse subdivision
        rects_coarse = axes.get_riemann_rectangles(
            curve,
            x_range=[1.0, 6.0],
            dx=1.0,
            input_sample_type="left",
            fill_opacity=0.3,
            stroke_width=1.5,
            stroke_color=ORANGE,
        )
        self.play(Create(rects_coarse))
        self.wait(1.5)
        
        # Refine Riemann partition
        rects_fine = axes.get_riemann_rectangles(
            curve,
            x_range=[1.0, 6.0],
            dx=0.25,
            input_sample_type="left",
            fill_opacity=0.4,
            stroke_width=0.5,
            stroke_color=ORANGE,
        )
        self.play(Transform(rects_coarse, rects_fine))
        self.wait(2.0)
        
        # Fade out Riemann elements
        self.play(
            FadeOut(rects_coarse), 
            FadeOut(riemann_title), 
            FadeOut(riemann_formula)
        )
        
        # 4. Lebesgue Partition (y-axis slicing)
        lebesgue_title = Text("Lebesgue: Slicing the Range (Y-Axis)", font_size=28, color=TEAL_C).to_edge(DOWN).shift(0.2 * UP)
        lebesgue_formula = MathTex(
            r"\int_a^b f(x) \, dx \approx \sum_j y_j \, \mu(E_j)", 
            font_size=32, 
            color=TEAL_C
        ).next_to(title, DOWN, buff=0.2)
        
        self.play(Write(lebesgue_title), Write(lebesgue_formula))
        self.wait(1.0)
        
        # Draw Lebesgue horizontal slices
        # For our function y = 3 - 0.5*(x-3.5)^2, the preimage of y is [3.5 - sqrt(2*(3-y)), 3.5 + sqrt(2*(3-y))]
        def get_lebesgue_slabs(num_slabs):
            slabs = VGroup()
            y_max = 3.0
            dy = y_max / num_slabs
            for j in range(num_slabs):
                yj = j * dy
                half_width = np.sqrt(2.0 * (3.0 - yj))
                x_start = 3.5 - half_width
                x_end = 3.5 + half_width
                
                # Create a rectangle representing the slab
                # In axes coordinates:
                p_bottom_left = axes.coords_to_point(x_start, yj)
                p_top_right = axes.coords_to_point(x_end, yj + dy)
                
                rect = Rectangle(
                    width=p_top_right[0] - p_bottom_left[0],
                    height=p_top_right[1] - p_bottom_left[1],
                    fill_color=TEAL_D,
                    fill_opacity=0.35,
                    stroke_color=TEAL_C,
                    stroke_width=1.0,
                ).move_to((p_bottom_left + p_top_right) / 2.0)
                slabs.add(rect)
            return slabs
            
        slabs_coarse = get_lebesgue_slabs(6)
        self.play(Create(slabs_coarse))
        self.wait(1.5)
        
        slabs_fine = get_lebesgue_slabs(24)
        self.play(Transform(slabs_coarse, slabs_fine))
        self.wait(2.5)
        
        # 5. Conclusion
        self.play(
            FadeOut(slabs_coarse),
            FadeOut(lebesgue_title),
            FadeOut(lebesgue_formula),
            FadeOut(curve),
            FadeOut(curve_label),
            FadeOut(axes),
            FadeOut(title)
        )
        
        final_text = Text("The Odyssey of Integration continues...", font_size=36, color=BLUE_C)
        self.play(Write(final_text))
        self.wait(2.0)
        self.play(FadeOut(final_text))

from manim import *
import numpy as np


def convex_set_shape():
    shape = Ellipse(width=5.6, height=3.6, color=GREEN_C)
    fill = shape.copy().set_fill(GREEN_E, opacity=0.18).set_stroke(width=0)
    return VGroup(fill, shape)


class ProjectionUniquenessHQ(Scene):
    def construct(self):
        title = Text("Uniqueness of the metric projection", font_size=44, color=BLUE_C).to_edge(UP)
        stmt = MathTex(
            r"\forall y\in K,\quad \langle x_k-x,\;x_k-y\rangle\le 0",
            font_size=42,
            color=ORANGE,
        ).next_to(title, DOWN, buff=0.25)
        self.play(Write(title), FadeIn(stmt, shift=0.2 * DOWN))

        K = convex_set_shape().shift(2.1 * LEFT + 0.7 * DOWN)
        K_label = MathTex(r"K\subset\mathbb{R}^n\ \text{convex}", font_size=32, color=GREEN_C).next_to(K, DOWN)
        self.play(FadeIn(K[0]), Create(K[1]), Write(K_label))

        x = Dot(np.array([3.6, 0.5, 0]), color=YELLOW)
        xk = Dot(np.array([0.55, -0.05, 0]), color=RED_C)
        y = Dot(np.array([-1.6, 0.95, 0]), color=TEAL_C)
        z = Dot(np.array([-0.5, -1.25, 0]), color=PURPLE_C)

        labels = VGroup(
            MathTex("x", color=YELLOW, font_size=34).next_to(x, RIGHT),
            MathTex("x_k", color=RED_C, font_size=34).next_to(xk, UP + 0.15 * RIGHT),
            MathTex("y\\in K", color=TEAL_C, font_size=30).next_to(y, UP + 0.2 * LEFT),
            MathTex("z\\in K", color=PURPLE_C, font_size=30).next_to(z, DOWN + 0.2 * LEFT),
        )
        self.play(*[FadeIn(p) for p in [x, xk, y]], *[Write(labels[i]) for i in range(3)])

        v1 = Arrow(x.get_center(), xk.get_center(), buff=0.08, color=RED_B)
        v2 = Arrow(y.get_center(), xk.get_center(), buff=0.08, color=TEAL_B)
        right_angle_hint = Angle(Line(xk.get_center(), x.get_center()), Line(xk.get_center(), y.get_center()), radius=0.35, color=ORANGE)
        self.play(GrowArrow(v1), GrowArrow(v2), Create(right_angle_hint))

        geo = Text(
            "Projection condition: every feasible direction in K\nmakes an obtuse angle with x_k - x.",
            font_size=24,
        ).to_edge(RIGHT).shift(0.8 * DOWN)
        self.play(FadeIn(geo, shift=0.2 * UP))
        self.wait(0.6)

        # Contradiction proof block
        self.play(FadeIn(z), Write(labels[3]))
        assume = MathTex(r"\text{Assume }z\in K\text{ is another projection}", font_size=32, color=PURPLE_C).to_edge(LEFT).shift(2.4 * UP)
        eq1 = MathTex(r"\langle x_k-x,\;x_k-z\rangle\le 0", font_size=36)
        eq2 = MathTex(r"\langle z-x,\;z-x_k\rangle\le 0", font_size=36)
        eq3 = MathTex(r"\Rightarrow\ \|x_k-z\|^2\le 0", font_size=38, color=ORANGE)
        eq4 = MathTex(r"\|x_k-z\|=0\Rightarrow z=x_k", font_size=44, color=RED_C)
        block = VGroup(eq1, eq2, eq3, eq4).arrange(DOWN, aligned_edge=LEFT, buff=0.26).next_to(assume, DOWN, aligned_edge=LEFT)

        self.play(Write(assume))
        self.play(Write(eq1))
        self.play(Write(eq2))
        self.play(Write(eq3))
        self.play(Write(eq4))

        conclusion = Text("Hence x_k is the unique projection of x onto K.", font_size=36, color=BLUE_C).to_edge(DOWN)
        self.play(Create(SurroundingRectangle(eq4, color=RED_C, buff=0.18)), Write(conclusion))
        self.wait(1.8)


class NormalConeInterpretation(Scene):
    def construct(self):
        title = Text("Equivalent normal-cone interpretation", font_size=42, color=BLUE_C).to_edge(UP)
        self.play(Write(title))

        K = convex_set_shape().shift(2.0 * LEFT + 0.6 * DOWN)
        self.play(FadeIn(K[0]), Create(K[1]))

        x = Dot(np.array([3.5, 0.35, 0]), color=YELLOW)
        xk = Dot(np.array([0.6, -0.1, 0]), color=RED_C)
        self.play(FadeIn(x), FadeIn(xk))
        self.play(
            Write(MathTex("x", color=YELLOW, font_size=32).next_to(x, RIGHT)),
            Write(MathTex("x_k", color=RED_C, font_size=32).next_to(xk, UP + 0.1 * RIGHT)),
        )

        normal_ray = Arrow(xk.get_center(), x.get_center(), buff=0.08, color=RED_B)
        tangent1 = Arrow(xk.get_center(), xk.get_center() + np.array([-1.5, 0.7, 0]), buff=0, color=TEAL_B)
        tangent2 = Arrow(xk.get_center(), xk.get_center() + np.array([-1.2, -0.8, 0]), buff=0, color=TEAL_B)
        self.play(GrowArrow(normal_ray), GrowArrow(tangent1), GrowArrow(tangent2))

        cone = VGroup(tangent1.copy().set_opacity(0.2), tangent2.copy().set_opacity(0.2))
        self.play(FadeIn(cone))

        eqA = MathTex(
            r"\langle x_k-x,\;x_k-y\rangle\le0\ \forall y\in K",
            font_size=38,
        ).to_edge(RIGHT).shift(0.4 * UP)
        eqB = MathTex(
            r"x-x_k\in N_K(x_k)",
            font_size=44,
            color=ORANGE,
        ).next_to(eqA, DOWN, buff=0.45)
        eqC = MathTex(
            r"\text{Projection} \Longleftrightarrow \text{normal cone condition}",
            font_size=34,
            color=BLUE_C,
        ).next_to(eqB, DOWN, buff=0.45)

        self.play(Write(eqA))
        self.play(TransformFromCopy(normal_ray, eqB))
        self.play(Write(eqC))
        self.wait(2)

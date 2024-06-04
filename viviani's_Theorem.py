import math
from manim import *

class Vivianis_Theorem(Scene):
    def construct(self):
        colors = [RED, GREEN, YELLOW]
        text_color = "#ffd5c0"
        side_length = 7
        shift_down = 3
        radius = 1.5
        A = UP * math.sqrt(side_length ** 2 - (side_length / 2) ** 2) + DOWN * 3
        B = LEFT * side_length / 2 + DOWN * 3
        C = RIGHT * side_length / 2 + DOWN * 3
        A_dot = Dot(A)
        B_dot = Dot(B)
        C_dot = Dot(C)
        AB = Line(A, B, color=BLUE)
        BC = Line(B, C, color=BLUE)
        AC = Line(C, A, color=BLUE)
        circle = Circle(radius=radius).shift(DOWN)
        D = Dot(circle.get_start())
        def create_perpendicular():
            line1 = Line(AB.get_projection(D.get_center()), D.get_center(), color=colors[0], stroke_width=8)
            line2 = Line(BC.get_projection(D.get_center()), D.get_center(), color=colors[1], stroke_width=8)
            line3 = Line(AC.get_projection(D.get_center()), D.get_center(), color=colors[2], stroke_width=8)
            angle1 = RightAngle(AB, line1, color=colors[0], length=0.25)
            angle2 = RightAngle(BC, line2, color=colors[1], length=0.25)
            angle3 = RightAngle(AC, line3, color=colors[2], length=0.25)
            return VGroup(line1, line2, line3, angle1, angle2, angle3)

        line = always_redraw(create_perpendicular)

        def create_sum():
            line1 = line[1].copy()
            line1.move_to(ORIGIN).align_to(BC, DOWN).shift(LEFT * 4)
            line2 = line[0].copy().rotate(120 * DEGREES).next_to(line1, UP, buff=0)
            line3 = line[2].copy().rotate(60 * DEGREES).next_to(line2, UP, buff=0)

            return VGroup(line1, line2, line3)

        sum = always_redraw(create_sum)
        dash_line1 = DashedLine(A, A + LEFT * 5, dashed_ratio=0.3, dash_length=0.07)
        dash_line2 = DashedLine(B, B + LEFT * 1.5, dashed_ratio=0.3, dash_length=0.07)
        text4 = MarkupText("Viviani's Theorem:", font_size=45, font="Sans", color=YELLOW).move_to(UP*3+RIGHT*4)
        self.play(Create(AB), Create(BC), Create(AC))
        self.wait()
        self.play(MoveAlongPath(D, circle, run_time=3), rate_func=linear)
        self.play(LaggedStart(*[
            Create(i) for i in line
        ], lag_ratio=0.3))
        self.add(line)
        self.play(MoveAlongPath(D, circle), run_time=3, rate_func=linear)
        self.add(sum, dash_line1, dash_line2)
        self.play(Write(text4), MoveAlongPath(D, circle), run_time=3, rate_func=linear)
        self.play(MoveAlongPath(D, circle), run_time=3, rate_func=linear)
        self.play(MoveAlongPath(D, circle), run_time=3, rate_func=linear)
        self.play(MoveAlongPath(D, circle), run_time=3, rate_func=linear)
        self.play(MoveAlongPath(D, circle), run_time=3, rate_func=linear)
        a = VGroup(AB, BC, AC, text4, sum, dash_line1, dash_line2, line, D)
        self.play(FadeOut(a))

        h_color = "#31c2fc"
        colors = [RED, GREEN, YELLOW, h_color]
        side_length = 7
        shift_down = 3
        radius = 1.5
        A = UP * math.sqrt(side_length ** 2 - (side_length / 2) ** 2) + DOWN * 3 + LEFT * 2 + UP * 0.3
        B = LEFT * side_length / 2 + DOWN * 3 + LEFT * 2 + UP * 0.3
        C = RIGHT * side_length / 2 + DOWN * 3 + LEFT * 2 + UP * 0.3
        A_dot = Dot(A)
        B_dot = Dot(B)
        C_dot = Dot(C)
        AB = Line(A, B)
        BC = Line(B, C)
        AC = Line(C, A)
        P = Dot(RIGHT * 1 + DOWN * 1.25 + LEFT * 2)

        def create_perpendicular():
            line1 = Line(AB.get_projection(P.get_center()), P.get_center(), color=colors[0])
            angle1 = RightAngle(AB, line1, color=colors[0], length=0.25)
            line2 = Line(BC.get_projection(P.get_center()), P.get_center(), color=colors[1])
            angle2 = RightAngle(BC, line2, color=colors[1], length=0.25)
            line3 = Line(AC.get_projection(P.get_center()), P.get_center(), color=colors[2])
            angle3 = RightAngle(AC, line3, color=colors[2], length=0.25)
            a = MathTex("a", color=colors[0]).scale(1).next_to(line1.get_center(), UR, buff=0.2)
            b = MathTex("b", color=colors[1]).scale(1).next_to(line2.get_center(), LEFT, buff=0.1)
            c = MathTex("c", color=colors[2]).scale(1).next_to(line3.get_center(), UL, buff=0.2)
            return VGroup(line1, line2, line3, angle1, angle2, angle3, a, b, c)

        def create_edge():
            line1 = Line(P.get_center(), A)
            line2 = Line(P.get_center(), B)
            line3 = Line(P.get_center(), C)
            return VGroup(line1, line2, line3)

        edge = create_edge()
        dash_line1 = DashedLine(A, A + LEFT * 3.7, dashed_ratio=0.3, dash_length=0.07)
        dash_line2 = DashedLine(B, B + LEFT * 0.2, dashed_ratio=0.3, dash_length=0.07)
        brace1 = Brace(VGroup(dash_line1, dash_line2), LEFT)
        brace2 = Brace(BC, DOWN)

        def create_tri_group0():
            tri1 = Polygon(A, P.get_center(), B, color=colors[0], fill_opacity=0.3, fill_color=colors[0])
            tri2 = Polygon(B, P.get_center(), C, color=colors[1], fill_opacity=0.3, fill_color=colors[1])
            tri3 = Polygon(A, P.get_center(), C, color=colors[2], fill_opacity=0.3, fill_color=colors[2])
            group = VGroup(tri1, tri3, tri2)
            return group

        def create_tri_group():
            add = MathTex("+").scale(8)
            tri1 = Polygon(A, P.get_center(), B, color=colors[0], fill_opacity=0.3, fill_color=colors[0])
            tri2 = Polygon(B, P.get_center(), C, color=colors[1], fill_opacity=0.3, fill_color=colors[1])
            tri3 = Polygon(A, P.get_center(), C, color=colors[2], fill_opacity=0.3, fill_color=colors[2])
            group = VGroup(tri1, add.copy(), tri2, add.copy(), tri3).scale(0.22).arrange(RIGHT)
            return group

        group_tri = create_tri_group().shift(UP * 2.5 + RIGHT * 2)
        result = MathTex("=", "{x", ".", "h", "\over", "2}").scale(1.5).next_to(group_tri, RIGHT)
        result[3].set_color(h_color)

        def create_abc():
            a = MathTex("{x", ".", "a", "\over", "2}", color=colors[0]).scale(1.5)
            a.move_to(group_tri[0])
            b = MathTex("{x", ".", "b", "\over", "2}", color=colors[1]).scale(1.5)
            b.move_to(group_tri[2])
            c = MathTex("{x", ".", "c", "\over", "2}", color=colors[2]).scale(1.5)
            c.move_to(group_tri[4])
            return VGroup(a, b, c)

        abc = create_abc()

        perpendicular = create_perpendicular()
        x = MathTex("x").scale(1.5).next_to(brace2, DOWN)
        h = MathTex("h", color=h_color).scale(1.5).next_to(brace1, LEFT)
        result1 = MathTex(r"\rightarrow", "a", "+", "b", "+", "c", "=", "h").scale(1.5).shift(RIGHT * 3)
        for i, j in zip((1, 3, 5, 7), colors):
            result1[i].set_color([j])
        group0 = create_tri_group0()
        self.play(Create(AB), Create(BC), Create(AC), Create(P))
        self.play(FadeIn(P), LaggedStart(*[
            Create(i) for i in edge
        ]))
        self.play(LaggedStart(*[
            Create(i) for i in group0
        ]))

        self.play(LaggedStart(*[
            ReplacementTransform(group0[0].copy(), group_tri[0]),
            ReplacementTransform(group0[2].copy(), group_tri[2]),
            ReplacementTransform(group0[1].copy(), group_tri[4]),
        ], lag_ratio=0.5))
        self.play(FadeIn(brace2, shift=UP), FadeIn(x, shift=UP))
        self.play(FadeIn(brace1, shift=RIGHT), FadeIn(h, shift=RIGHT), Create(dash_line1), Create(dash_line2))
        self.play(LaggedStart(*[
            FadeIn(group_tri[1], shift=UP),
            FadeIn(group_tri[3], shift=UP),
            FadeIn(result[0], shift=UP)
        ], lag_ratio=0.3))
        self.play(LaggedStart(*[
            Transform(x.copy(), result[1]),
            Transform(h.copy(), result[3]),
            FadeIn(result[2]), FadeIn(result[4]), FadeIn(result[5])
        ], lag_ratio=0.5))
        self.play(*[FadeOut(i) for i in (group0)])
        self.play(LaggedStart(*[
            Create(i) for i in perpendicular
        ]))
        for i, j in zip((group_tri[0], group_tri[2], group_tri[4]), abc):
            self.play(Transform(i, j))
        self.play(Write(result1))
        self.play(Circumscribe(result1))
        self.wait()

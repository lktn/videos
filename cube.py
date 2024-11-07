from manim import *
import numpy as np

config.pixel_height = 1920
config.pixel_width = 1080

class Cubes(ThreeDScene):
    def construct(self):
        a = 6
        b = a*(3-5**0.5)/4
        c = a*(5**0.5-1)/4
        d = a*(5**0.5-2)/2
        e = 0.9
        
        a0 = ThreeDAxes()
        a1 = Cube(side_length=a, color=WHITE, stroke_width=3, fill_opacity=0)
        a2 = Cube(side_length=2*c, color="#00EEAC", fill_color="#00EEAC", fill_opacity=e).move_to([-b, +b, -b])

        a3 = Prism(dimensions=[2*c, 2*b, 2*c], fill_color=BLUE, fill_opacity=e).move_to([-b, -c, -b])
        a4 = Prism(dimensions=[2*b, 2*c, 2*c], fill_color=BLUE, fill_opacity=e).move_to([+c, +b, -b])
        a5 = Prism(dimensions=[2*c, 2*c, 2*b], fill_color=BLUE, fill_opacity=e).move_to([-b, +b, +c])

        a6 = Prism(dimensions=[2*b, 2*b, 2*c], fill_color="#9586CD", fill_opacity=e).move_to([+c, -c, -b])
        a7 = Prism(dimensions=[2*c, 2*b, 2*b], fill_color="#9586CD", fill_opacity=e).move_to([-b, -c, +c])
        a8 = Prism(dimensions=[2*b, 2*c, 2*b], fill_color="#9586CD", fill_opacity=e).move_to([+c, +b, +c])

        a9 = Cube(side_length=2*b, color=PINK, fill_color=PINK, fill_opacity=0.5).move_to([+c, -c, +c])
        self.set_camera_orientation(phi=60 * DEGREES, theta=-60 * DEGREES)

        b1 = VGroup(Line(start=np.array([-a/2, -a/2, -a/2]), end=np.array([d, -a/2, -a/2]), stroke_width=10, color=BLUE),
                    Line(start=np.array([+a/2, -a/2, -a/2]), end=np.array([d, -a/2, -a/2]), stroke_width=10, color="#9586CD"))
        b2 = VGroup(Line(start=np.array([+a/2, +a/2, -a/2]), end=np.array([a/2, -d, -a/2]), stroke_width=10, color=BLUE),
                    Line(start=np.array([+a/2, -a/2, -a/2]), end=np.array([a/2, -d, -a/2]), stroke_width=10, color="#9586CD"))
        b3 = VGroup(Line(start=np.array([-a/2, -a/2, -a/2]), end=np.array([-a/2, -a/2, d]), stroke_width=10, color=BLUE),
                    Line(start=np.array([-a/2, -a/2, +a/2]), end=np.array([-a/2, -a/2, d]), stroke_width=10, color="#9586CD"))

        self.play(GrowFromCenter(a1))
        self.play(GrowFromCenter(b1), GrowFromCenter(b2), GrowFromCenter(b3))

        a10 = Brace(b1[0], -UP, stroke_width=6)
        a11 = MathTex("a").next_to(a10, -UP, buff=0.3).scale(1.5)
        a12 = Brace(b1[1], -UP, stroke_width=6)
        a13 = MathTex("b").next_to(a12, -UP, buff=0.3).scale(1.5)

        a14 = Brace(b2[0], -LEFT, stroke_width=6)
        a15 = MathTex("a").next_to(a14, -LEFT, buff=0.3).scale(1.5)
        a16 = Brace(b2[1], -LEFT, stroke_width=6)
        a17 = MathTex("b").next_to(a16, -LEFT, buff=0.3).scale(1.5)

        a18 = a0.get_z_axis_label(MathTex(r"\begin{cases}\\\\\\\\\\\end{cases}", stroke_width=6)).move_to(LEFT*a/2-(a/2+0.4)*UP-1.13*OUT).rotate(PI/2).scale(1.038)
        a19 = MathTex("a").next_to(a18, -UP, buff=0.3).scale(1.5).rotate(90*DEGREES).rotate(90*DEGREES, axis=UP)
        a20 = a0.get_z_axis_label(MathTex(r"\begin{cases}\\\\\\\end{cases}", stroke_width=6)).next_to(a18, OUT, buff=0.07).rotate(PI/2).scale(1.08)
        a21 = MathTex("b").next_to(a20, -UP, buff=0.3).scale(1.5).rotate(90*DEGREES).rotate(90*DEGREES, axis=UP)

        self.play(
            FadeIn(VGroup(a10, a11, a12, a13), shift=2*UP),
            FadeIn(VGroup(a14, a15, a16, a17), shift=2*LEFT),
            FadeIn(VGroup(a18, a19, a20, a21), shift=2*UP)
        )

        f1 = MathTex("(a+b)^3=", "a^3", "+3a^2b", "+3ab^2", "+b^3").scale(1.5).move_to(-8*UP)
        self.add_fixed_in_frame_mobjects(f1[0])
        self.play(Write(f1[0]))
        self.wait()

        self.play(GrowFromCenter(a2), run_time=1)
        self.add_fixed_in_frame_mobjects(f1[1])
        self.play(Write(f1[1]))
        self.wait()

        self.play(GrowFromCenter(a3), GrowFromCenter(a4), GrowFromCenter(a5), run_time=1)
        self.add_fixed_in_frame_mobjects(f1[2])
        self.play(Write(f1[2]))
        self.wait()

        self.play(GrowFromCenter(a6), GrowFromCenter(a7), GrowFromCenter(a8), run_time=1)
        self.add_fixed_in_frame_mobjects(f1[3])
        self.play(Write(f1[3]))
        self.wait()

        self.play(GrowFromCenter(a9), run_time=1)
        self.add_fixed_in_frame_mobjects(f1[4])
        self.play(Write(f1[4]))
        self.wait()
        self.add_fixed_in_frame_mobjects(f1)
        self.wait()

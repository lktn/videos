from manim import *
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 8
config.frame_width = 4.5
class RotateTriangles(Scene):
    def construct(self):
        a = [0, (3**0.5)/2, 0]
        b = [-0.5, 0, 0]
        c = [0.5, 0, 0]
        d = [(3**0.5-2)/4, -(4*3**0.5-3)**0.5/4, 0]
        e = [(18-6*(4*3**0.5-3)**0.5-3*3**0.5)/12, ((4*3**0.5-3)**0.5-2*3**0.5)/4, 0]
        f = [-1, (-3**0.5)/2, 0]
        g = [(1-(4*3**0.5-3)**0.5)/2, (-3**0.5)/2, 0]
        h = [(3-(4*3**0.5-3)**0.5)/2, (-3**0.5)/2, 0]
        j = [1, (-3**0.5)/2, 0]

        a1 = Polygon(g, h, e, color=RED, fill_opacity=1, stroke_width=0)
        a2 = Polygon(c, e, h, j, color=YELLOW, fill_opacity=1, stroke_width=0)
        a3 = Polygon(a, b, d, c, color=GREEN, fill_opacity=1, stroke_width=0)
        a4 = Polygon(b, f, g, d, color=BLUE, fill_opacity=1, stroke_width=0)

        f1 = Tex("A triangle is").move_to(UP*2.75).scale(0.8)
        f2 = Tex("a square").move_to(UP*2.25).scale(0.8)

        nhom = VGroup(a1, a2, a3, a4, f1)

        def ab(t):
            return t**2

        def ba(t):
            return  2*t-t**2

        self.play(DrawBorderThenFill(nhom))
        self.play(Rotate(VGroup(a1, a2, a4), angle=-PI, about_point=b), rate_func=ab)
        self.play(Rotate(VGroup(a1, a2), angle=-PI, about_point=[((4*3**0.5-3)**0.5-3)/2, (3**0.5)/2, 0], rate_func=linear))
        self.play(Rotate(VGroup(a2), angle=-PI, about_point=[((4*3**0.5-3)**0.5-1)/2, (3**0.5)/2, 0], rate_func=ba))
        self.add(f2)
        self.wait(3)

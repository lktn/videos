from manim import *
config.pixel_height = 1920*2
config.pixel_width = 1080*2
class MyScene(Scene):
    def construct(self):
        kwarg = {"side_length": 1, "fill_opacity": 0.5, "color": BLUE, "stroke_width": 6}
        v = VGroup()
        for i in range(-1, 5):
            for j in range(-1, i):
                v.add(Square(**kwarg).move_to([i-2, j-1, 0]))
                
        a = MathTex("2", "(", "1", "+2", "+3", "+\\cdots", "+n", ")", "=", "n", "(n+1)")
        a.move_to(-UP*7).scale(1.4)
        v.scale(1.3)
        self.play(GrowFromCenter(v[0]), Write(a[2]))
        for i in range(1, 5):
            self.play(
                *[GrowFromCenter(v[j]) for j in range(int(i*(i+1)/2), int((i+1)*(i+2)/2))],
                Write(a[i+2])
            )
        self.wait()
        g = v.copy()
        a1 = Brace(v, RIGHT, stroke_width=3)
        a2 = MathTex("n").next_to(a1, RIGHT, buff=0.3).scale(1.4)
        a3 = Brace(v, DOWN, stroke_width=3)
        a4 = MathTex("n").next_to(a3, DOWN, buff=0.3).scale(1.4)
        self.play(FadeIn(VGroup(a1, a2), shift=2*LEFT), FadeIn(VGroup(a3, a4), shift=2*UP))
        self.wait()
        self.play(Rotate(g, angle=PI, about_point=[0, 0.65, 0]), FadeIn(VGroup(a[0], a[1], a[7], a[8])))
        self.wait()

        a5 = Brace(VGroup(v, g), RIGHT, stroke_width=3)
        a6 = MathTex("n+1").next_to(a5, RIGHT, buff=0.5).scale(1.4)
        self.play(ReplacementTransform(VGroup(a1, a2), VGroup(a5, a6)))
        self.wait()


        self.play(TransformFromCopy(a4, a[9]), TransformFromCopy(a6, a[10]))
        self.wait()

        a7 = MathTex(r"1+2+3+\cdots+n", "=", r"{n(n+1)", r"\over", r"2}").move_to(-UP*7).scale(1.4)
        self.play(
            VGroup(a[2], a[3], a[4], a[5], a[6]).animate.move_to(a7[0].get_center()),
            VGroup(a[9], a[10]).animate.move_to(a7[2].get_center()),
            a[8].animate.move_to(a7[1].get_center()),
            FadeOut(VGroup(a[1], a[7])),
            a[0].animate.move_to(a7[4].get_center()),
            FadeIn(a7[3])
            )
        self.wait()

        a8 = MathTex(r"\sum_{i=1}^ni", r"=\frac{n(n+1)}2").move_to(-UP*7).scale(1.4)
        self.play(
            VGroup(a[0], a[8], a[9], a[10], a7[3]).animate.move_to(a8[1].get_center()),
            ReplacementTransform(VGroup(a[2], a[3], a[4], a[5], a[6], a7[0]), a8[0])
            )
        self.wait()
        self.play(Circumscribe(a8))
        self.wait()
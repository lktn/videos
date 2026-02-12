from manim import *
import numpy as np
config.pixel_height = 1920*2
config.pixel_width = 1080*2
class BrahmaguptaFormula(Scene):
    def construct(self):
        phi = (1 + np.sqrt(5))/2
        k = 1.5*PI - (phi**3 + phi**4)/2

        dots = VGroup()
        points = []
        for i in range(1, 5):
            t = phi**i + k
            p = 4 * np.exp(t*1j)
            p = [-p.real, p.imag, 0]
            points.append(p)
            dots.add(Dot(p, radius=0.12))

        quad = Polygon(*points, stroke_width=8, color=BLUE)

        circle = Circle(radius=4, stroke_width=8)
        letters = VGroup(
            MathTex("d").scale(1.4).move_to([2.9, 1.7, 0]),
            MathTex("D").scale(1.4).move_to([1, 4.5, 0]),
            MathTex("a").scale(1.4).move_to([-0.8, 3, 0]),
            MathTex("A").scale(1.4).move_to([-3.4, 3.4, 0]),
            MathTex("b").scale(1.4).move_to([-2.9, 1, 0]),
            MathTex("B").scale(1.4).move_to([-4.5, -1.4, 0]),
            MathTex("c").scale(1.5).move_to([0, -1.6, 0]),
            MathTex("C").scale(1.4).move_to([4.4, -1.4, 0])
        )
        VGroup(dots, circle, letters, quad).shift(UP)
        self.play(GrowFromCenter(quad), run_time=1.5)
        self.play(Create(circle), Write(letters), Write(dots))

        e1 = MathTex("S=", "S_{ABD}", "+", "S_{BCD}")
        e2 = MathTex("S=", r"\frac12ab\sin A", "+", r"\frac12cd\sin C")
        e3 = MathTex(r"2S=ab\sin A+cd\sin", "C")
        e4 = MathTex(r"2S=ab\sin A+cd\sin", r"(\pi-A)")
        e5 = MathTex(r"2S=ab\sin A+cd\sin", "A")
        e6 = MathTex("2", r"S=(ab+cd)\sin A")
        e7 = MathTex("4", r"S^2=(ab+cd)^2", r"\sin^2A")
        e8 = MathTex(r"4S^2=(ab+cd)^2", r"(1-\cos^2A)")
        e9 = MathTex(r"4S^2=(ab+cd)^2-(ab+cd)^2\cos^2A").scale(0.8)
        e10 = MathTex(r"16S^2=4(ab+cd)^2-4(ab+cd)^2\cos^2A").scale(0.8)
        e11 = MathTex(r"16S^2=(2ab+2cd)^2-", r"(2ab+2cd)^2\cos^2A").scale(0.8)
        e12 = MathTex(r"16S^2=(2ab+2cd)^2-", r"(a^2+b^2-c^2-d^2)^2").scale(0.8)
        e13 = MathTex(
            r"16S^2&=\left(2ab+2cd-a^2-b^2+c^2+d^2\right)\\",
            r"&\times\left(2ab+2cd+a^2+b^2-c^2-d^2\right)"
        ).scale(0.8)
        e14 = MathTex(
            r"16S^2&=\left[(c+d)^2-(a-b)^2\right]\\", 
            r"&\times\left[(a+b)^2-(c-d)^2\right]"
        )
        e15 = MathTex(
            r"16S^2&=(c+d-a+b)(c+d+a-b)\\", 
            r"&\times(a+b-c+d)(a+b+c-d)"
        ).scale(0.85)
        e16 = MathTex("16S^2=(2p-2a)(2p-2b)(2p-2c)(2p-2d)").scale(0.8)
        e17 = MathTex("S^2=(p-a)(p-b)(p-c)(p-d)").scale(0.9)
        e18 = MathTex(r"S=\sqrt{(p-a)(p-b)(p-c)(p-d)}").scale(0.9)
        VGroup(
            e1,  e2,  e3,  e4,  e5,  e6,  
            e7,  e8,  e9,  e10, e11, e12, 
            e13, e14, e15, e16, e17, e18
        ).scale(1.4).move_to(6*DOWN)

        quad_copy = quad.copy()
        self.play(quad_copy.animate.set_fill(BLUE_E, opacity=0.6))
        self.play(ReplacementTransform(quad_copy, e1[0]))
        self.play(Write(VGroup(e1[1], e1[2], e1[3])))
        self.wait(0.5)
        self.play(
            TransformMatchingShapes(e1[0], e2[0]), 
            TransformMatchingShapes(e1[2], e2[2]),
            ReplacementTransform(e1[1], e2[1]),
            ReplacementTransform(e1[3], e2[3]),
        )
        self.wait(0.5)
        self.play(TransformMatchingShapes(e2, e3))
        self.wait(0.5)
        self.play(
            TransformMatchingShapes(e3[0], e4[0]),
            ReplacementTransform(e3[1], e4[1])
        )
        self.wait(0.5)
        self.play(
            TransformMatchingShapes(e4[0], e5[0]),
            ReplacementTransform(e4[1], e5[1])
        )
        self.wait(0.5)
        self.play(TransformMatchingShapes(e5, e6))
        self.wait(0.5)

        b1 = MathTex(r"&BD^2=c^2+d^2-2cd\cos", "C")
        b2 = MathTex(r"&BD^2=c^2+d^2-2cd\cos", r"(\pi-A)")
        b3 = MathTex(r"&BD^2=", r"c^2+d^2+2cd\cos A")
        b4 = MathTex(r"&BD^2", r"=a^2+b^2-2ab\cos A").shift(0.9*DOWN)
        b5 = MathTex(r"c^2+d^2+2cd\cos A=a^2+b^2-2ab\cos A").scale(0.85)
        b6 = MathTex(r"(2ab+2cd)\cos A=a^2+b^2-c^2-d^2").scale(0.85)
        b7 = MathTex("2p=a+b+c+d")
        b8 = MathTex(r"p=\frac{a+b+c+d}2").scale(0.9)
        VGroup(b1, b2, b3, b4, b5, b6, b7, b8).scale(1.4).shift(8*DOWN)

        self.play(Write(b1))
        self.wait(0.5)
        self.play(
            TransformMatchingShapes(b1[0], b2[0]),
            ReplacementTransform(b1[1], b2[1])
        )
        self.wait(0.5)
        self.play(TransformMatchingShapes(b2, b3))
        self.wait(0.5)
        self.play(Write(b4))
        self.wait(0.5)
        self.play(
            TransformMatchingShapes(VGroup(b3[1], b4[1]), b5),
            FadeOut(VGroup(b3[0], b4[0]), run_time=0.5)
        )
        self.wait(0.5)
        self.play(TransformMatchingShapes(b5, b6))
        self.wait(0.5)
        
        self.play(
            ReplacementTransform(e6[0], e7[0]),
            TransformMatchingShapes(e6[1], VGroup(e7[1], e7[2]))
        )
        self.wait(0.5)
        self.play(
            TransformMatchingShapes(VGroup(e7[0], e7[1]), e8[0]),
            ReplacementTransform(e7[2], e8[1])
        )
        self.wait(0.5)
        self.play(TransformMatchingShapes(e8, e9))
        self.wait(0.5)
        self.play(TransformMatchingShapes(e9, e10))
        self.wait(0.5)
        self.play(TransformMatchingShapes(e10, e11))
        self.wait(0.5)
        self.play(
            TransformMatchingShapes(e11[0], e12[0]),
            ReplacementTransform(e11[1], e12[1])
        )
        self.play(FadeOut(b6))
        self.play(TransformMatchingShapes(e12, e13))
        self.wait(0.5)
        self.play(TransformMatchingShapes(e13, e14))
        self.wait(0.5)
        self.play(TransformMatchingShapes(e14, e15))
        self.play(Write(b7))
        self.play(ReplacementTransform(e15, e16))
        self.wait(0.5)
        self.play(TransformMatchingShapes(e16, e17))
        self.wait(0.5)
        self.play(TransformMatchingShapes(e17, e18))
        self.wait(0.5)
        self.play(TransformMatchingShapes(b7, b8))
        self.play(Circumscribe(VGroup(e18, b8), stroke_width=6))
        self.wait(0.5)
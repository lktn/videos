from manim import *

config.pixel_height = 1920
config.pixel_width = 1080

class a(Scene):
    def construct(self):
        a1 = MathTex(r"ax^4+bx^3+cx^2+dx+e=0")
        a2 = MathTex(r"x", r"^4", r"+{b\over a}", r"x", r"^3", r"+", r"{c\over a}", r"x", r"^2", r"+{d\over a}", r"x", r"+{e\over a}=0")
        a3 = MathTex(r"x=y-{b\over 4a}").move_to(3.5*UP)
        a4 = MathTex(
            r"&\left(y-{b\over 4a}\right)", r"^4", r"+{b\over a}", r"\left(y-{b \over 4a}\right)", r"^3", r"+", r"{c\over a}", r"\left(y-{b \over 4a}\right)", r"^2 \\",
            r"&+{d\over a}", r"\left(y-{b\over 4a}\right)", r"+{e\over a}=0"
        )
        a5 = MathTex(
            r"&\left(y^4-{b\over a}y^3+{6y^2b^2\over 16a^2}-{4yb^3\over 64a^3}+{b^4\over 256a^4}\right)\\",
            r"&+{b\over a}", r"\left(y^3-{3y^2b \over 4a}+{3yb^2\over 16a^2}-{b^3\over 64a^3}\right)", r"+\\",
            r"&{c\over a}", r"\left(y^2-{yb\over 2a}+{b^2\over 16a^2}\right)", r"+{d\over a}\left(y-{b\over 4a}\right)+{e\over a}=0")

        b5 = MathTex(
            r"&y^4-{b\over a}y^3+{6b^2\over 16a^2}y^2-{4b^3\over 64a^3}y+{b^4\over 256a^4}+\frac{b}{a}y^3\\",
            r"&-\frac{3b^2}{4a^2}y^2+\frac{3b^3}{16a^3}y-\frac{b^4}{64a^4}+\frac{c}{a}y^2-\frac{bc}{2a^2}y\\",
            r"&+\frac{b^2c}{16a^3}+\frac{d}{a}y-\frac{bd}{4a^2}+\frac{e}{a}=0"
        )
        a6 = MathTex(
            r"&y^4+", r"\bigg(", r"{-3b^2\over 8a^2}+{c\over a}", r"\bigg)", r"y^2+", r"\bigg(", r"{b^3\over 8a^3}-{bc\over 2a^2}+{d\over a}", r"\bigg)", r"y\\",
            r"&+", r"{-3b^4\over 256a^4}+{b^2c\over 16a^3}-{bd\over 4a^2}+{e\over a}", r"=0"
        )
        b6 = MathTex(
            r"&y^4+", r"\bigg(", r"{8ac-3b^2\over 8a^2}", r"\bigg)", r"y^2+", r"\bigg(", r"{b^3-4abc+8a^2d\over 8a^3}", r"\bigg)", r"y\\",
            r"&+", r"{16ab^2c-64a^2bd-3b^4+256a^3e\over 256a^4}", r"=0"
        )
        a7 =MathTex(
            r"&p=", r"{8ac-3b^2\over 8a^2}\\",
            r"&q=", r"{b^3-4abc+8a^2d\over 8a^3}\\",
            r"&r=", r"{16ab^2c-64a^2bd-3b^4+256a^3e\over 256a^4}").move_to(UP*6.75)
        a8 = MathTex(r"y^4+", r"p", r"y^2+", r"q", r"y", r"+", r"r", r"=0")
        a9 = MathTex(r"y^4+py^2=-qy-r")
        a10 = MathTex(r"y^4+2py^2+p^2", r"=", r"-qy", r"-r", r"+py^2", r"+p^2")
        a11 = MathTex(r"(y^2+p)^2", r"=", r"+py^2", r"-qy", r"-r", r"+p^2")
        a12 = MathTex(
            r"&(y^2+p)^2", r"+2(y^2+p)z+z^2", r"=\\", 
            r"&py^2", r"-qy", r"-r", r"+p^2", r"+2(y^2+p)z+z^2")
        a13 = MathTex(
            r"&(y^2+p+z)^2=\\", r"&(", r"p+2z", r")", r"y^2", r"-q", r"y+(", r"p^2-r+2pz+z^2", r")\\", 
            r"&\Delta =", r"(", r"-q", r")", r"^2-4(", r"p+2z", r")(", r"p^2-r+2pz+z^2", r")=0"
        )
        a14 = MathTex(r"8z^3+20pz^2+(16p^2-8r)z+4p^3-4pr-q^2=0").move_to(-1.6*UP).scale(1.1)
        a15 = MathTex(r"A=8\ \ B=20p\ \ C=16p^2-8r\ \ D=4p^3-4pr-q^2").move_to(4.5*UP)
        a16 = MathTex(r"z=\sqrt[3]{\frac{-B^3}{27A^3}+\frac{BC}{6A^2}-\frac{D}{2A}+\sqrt{\left(\frac{-B^3}{27A^3}+\frac{BC}{6A^2}-\frac{D}{2A}\right)^2+\left(\frac{C}{3A}-\frac{B^2}{9A^2}\right)^3}}+\\\sqrt[3]{\frac{-B^3}{27A^3}+\frac{BC}{6A^2}-\frac{D}{2A}-\sqrt{\left(\frac{-B^3}{27A^3}+\frac{BC}{6A^2}-\frac{D}{2A}\right)^2+\left(\frac{C}{3A}-\frac{B^2}{9A^2}\right)^3}}-\frac{B}{3A}").scale(0.8).move_to(2.25*UP)
        a17 = MathTex(r"(y^2+p+z)^2=\left(\sqrt{p+2z}\ y-\frac{q}{2\sqrt{p+2z}}\right)^2").move_to(-1.8*UP)
        a18 = MathTex(r"(y^2+p+z)^2-\left(\sqrt{p+2z}\ y-\frac{q}{2\sqrt{p+2z}}\right)^2=0").move_to(-1.8*UP)
        a19 = MathTex(
            r"&\bigg(y^2", r"+p+z", r"-\sqrt{p+2z}\ y+\frac{q}{2\sqrt{p+2z}}", r"\bigg)\cdot\\",
            r"&\bigg(y^2", r"+p+z", r"+\sqrt{p+2z}\ y-\frac{q}{2\sqrt{p+2z}}", r"\bigg)=0").move_to(-1.8*UP)
        a20 = MathTex(
            r"&\bigg(y^2", r"-\sqrt{p+2z}\ y+\frac{q}{2\sqrt{p+2z}}", r"+p+z", r"\bigg)\cdot\\",
            r"&\bigg(y^2", r"+\sqrt{p+2z}\ y-\frac{q}{2\sqrt{p+2z}}", r"+p+z", r"\bigg)=0").move_to(-1.8*UP)
        a21 = MathTex(
            r"&y^2-\sqrt{p+2z}\ y+\frac{q}{2\sqrt{p+2z}}+p+z=0\\",
            r"&y^2+\sqrt{p+2z}\ y-\frac{q}{2\sqrt{p+2z}}+p+z=0").move_to(-1.8*UP)
        a22 = MathTex(
            r"&y_{1,2}=+\frac{\sqrt{p+2z}}{2}\pm\sqrt{\frac{-q}{2\sqrt{p+2z}}-\frac{3p+2z}{4}}\\",
            r"&y_{3,4}=-\frac{\sqrt{p+2z}}{2}\pm\sqrt{\frac{q}{2\sqrt{p+2z}}-\frac{3p+2z}{4}}").move_to(-1.8*UP)
        a23 = MathTex(
            r"x_{1,2}=-\frac{b}{4a}+\frac{\sqrt{p+2z}}{2}\pm\sqrt{\frac{-q}{2\sqrt{p+2z}}-\frac{3p+2z}{4}}\\",
            r"x_{3,4}=-\frac{b}{4a}-\frac{\sqrt{p+2z}}{2}\pm\sqrt{\frac{q}{2\sqrt{p+2z}}-\frac{3p+2z}{4}}").scale(0.9).move_to(-1.8*UP)
        a = VGroup(a1, a2, a3, a4, a5, b5, a6, b6, a7, a8, a9, a10, a11, a12, a13).scale(1.2).set_stroke(width=1)
        b = VGroup(a14, a15, a16, a17, a18, a19, a20, a21, a22, a23).set_stroke(width=1)

        self.play(Write(a1))
        self.play(TransformMatchingShapes(a1, a2))
        self.play(Write(a3))
        self.play(ReplacementTransform(a2[i], a4[i]) for i in range(len(a2))) 
        self.wait(0.5)
        self.play(
            ReplacementTransform(VGroup(a4[0], a4[1]), a5[0]), 
            ReplacementTransform(a4[2], a5[1]),
            ReplacementTransform(VGroup(a4[3], a4[4]), a5[2]), 
            ReplacementTransform(a4[5], a5[3]),
            ReplacementTransform(a4[6], a5[4]), 
            ReplacementTransform(VGroup(a4[7], a4[8]), a5[5]),
            TransformMatchingShapes(VGroup(a4[9], a4[10], a4[11]), a5[6])
        )
        self.wait(0.5)
        self.play(ReplacementTransform(a5, b5))
        self.wait(0.5)
        self.play(ReplacementTransform(b5, a6))
        self.wait(0.5)
        self.play(ReplacementTransform(a6[i], b6[i]) for i in range(len(a6)))
        self.wait(0.5)
        self.play(
            Write(a7[0]),
            Write(a7[2]),
            Write(a7[4]),
            TransformFromCopy(b6[2], a7[1]),
            TransformFromCopy(b6[6], a7[3]),
            TransformFromCopy(b6[10], a7[5]), 
            a3.animate.shift(3.3*RIGHT+5.4*UP)
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(b6[0], a8[0]),
            ReplacementTransform(VGroup(b6[1], b6[2], b6[3]), a8[1]),
            ReplacementTransform(b6[4], a8[2]),
            ReplacementTransform(VGroup(b6[5], b6[6], b6[7]), a8[3]),
            ReplacementTransform(b6[8], a8[4]),
            ReplacementTransform(b6[9], a8[5]),
            ReplacementTransform(b6[10], a8[6]),
            ReplacementTransform(b6[11], a8[7]),
        )
        self.wait(0.5)
        self.play(TransformMatchingShapes(a8, a9))
        self.wait(0.5)
        self.play(TransformMatchingShapes(a9, a10))
        self.wait(0.5)
        self.play(
            ReplacementTransform(a10[0], a11[0]),
            ReplacementTransform(a10[1], a11[1]),
            ReplacementTransform(a10[2], a11[3]),
            ReplacementTransform(a10[3], a11[4]),
            ReplacementTransform(a10[4], a11[2]),
            ReplacementTransform(a10[5], a11[5]),
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(a11[0], a12[0]),
            ReplacementTransform(a11[1], a12[2]),
            ReplacementTransform(a11[2], a12[3]),
            ReplacementTransform(a11[3], a12[4]),
            ReplacementTransform(a11[4], a12[5]),
            ReplacementTransform(a11[5], a12[6]),
        )
        self.play(Write(a12[1]), Write(a12[7]))
        self.wait(0.5)
        k = VGroup(a13[0], a13[1], a13[2], a13[3], a13[4], a13[5], a13[6], a13[7], a13[8])
        self.play(TransformMatchingShapes(a12, k))
        self.wait(0.5)
        b = VGroup(a13[9], a13[10], a13[12], a13[13], a13[15], a13[17])
        self.play(Write(b))
        self.wait(0.5)
        self.play(TransformFromCopy(a13[5], a13[11]), TransformFromCopy(a13[2], a13[14]), TransformFromCopy(a13[7], a13[16]))
        self.wait(0.5)
        c = VGroup(a13[9], a13[10], a13[11], a13[12], a13[13], a13[14], a13[15], a13[16], a13[17])
        self.play(ReplacementTransform(c, a14))
        self.wait(0.5)
        self.play(Write(VGroup(a15, a16)))
        self.wait(0.5)
        self.play(FadeOut(a14))
        self.wait(0.5)
        self.play(ReplacementTransform(k, a17))
        self.wait(0.5)
        self.play(TransformMatchingShapes(a17, a18))
        self.wait(0.5)
        self.play(TransformMatchingShapes(a18, a19))
        self.wait(0.5)
        self.play(
            TransformMatchingShapes(a19[0], a20[0]),
            TransformMatchingShapes(a19[1], a20[2]),
            TransformMatchingShapes(a19[2], a20[1]),
            TransformMatchingShapes(a19[3], a20[3]),
            TransformMatchingShapes(a19[4], a20[4]),
            TransformMatchingShapes(a19[5], a20[6]),
            TransformMatchingShapes(a19[6], a20[5]),
            TransformMatchingShapes(a19[7], a20[7])
        )
        self.wait(0.5)
        self.play(TransformMatchingShapes(VGroup(a20[0], a20[1], a20[2], a20[3]), a21[0]), TransformMatchingShapes(VGroup(a20[4], a20[5], a20[6], a20[7]), a21[1]))
        self.wait(0.5)
        self.play(TransformMatchingShapes(a21[0], a22[0]), TransformMatchingShapes(a21[1], a22[1]))
        self.wait(0.5)
        self.play(TransformMatchingShapes(a22[0], a23[0]), TransformMatchingShapes(a22[1], a23[1]), FadeOut(a3))
        self.wait(0.5)
        self.play(Circumscribe(a23))
        self.wait(1)
        self.play(FadeOut(VGroup(a7, a15, a16, a23[0], a23[1])))
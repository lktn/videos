from manim import *
config.pixel_height = 1920
config.pixel_width = 1080
class Hyperbol(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-3, 3],
            x_length=4*PI,
            y_length=2.4*PI
        )

        sinh = MathTex(r"y=\sinh(x)")
        cosh = MathTex(r"y=\cosh(x)")
        tanh = MathTex(r"y=\tanh(x)")
        csch = MathTex(r"y=\text{csch}(x)")
        sech = MathTex(r"y=\text{sech}(x)")
        coth = MathTex(r"y=\text{coth}(x)")
        arcsinh = MathTex(r"y=\text{arcsinh}(x)")
        arccosh = MathTex(r"y=\text{arccosh}(x)")
        arctanh = MathTex(r"y=\text{arctanh}(x)")
        arccsch = MathTex(r"y=\text{arccsch}(x)")
        arcsech = MathTex(r"y=\text{arcsech}(x)")
        arccoth = MathTex(r"y=\text{arccoth}(x)")
        
        v = VGroup(sinh, cosh, tanh, csch, sech, coth, arcsinh, arccosh, arctanh, arccsch, arcsech, arccoth)
        v.move_to(UP*5.5).scale(1.3).set_z_index(2)

        a = {"color": BLUE, "x_range": [-6, 6, 0.01]}
        a1 = axes.plot(lambda x: np.sinh(x), **a)
        a2 = axes.plot(lambda x: np.cosh(x), **a)
        a3 = axes.plot(lambda x: np.tanh(x), **a)
        a4 = VGroup(
            axes.plot(lambda x: 1/np.sinh(x), x_range=[-6, -0.01, 0.01]),
            axes.plot(lambda x: 1/np.sinh(x), x_range=[+0.01, +6, 0.01])
        ).set_z_index(1)
        a5 = axes.plot(lambda x: 1/np.cosh(x), **a)
        a6 = VGroup(
            axes.plot(lambda x: np.cosh(x)/np.sinh(x), x_range=[-6, -0.01, 0.01]),
            axes.plot(lambda x: np.cosh(x)/np.sinh(x), x_range=[+0.01, +6, 0.01])
        ).set_z_index(1)
        a7 = axes.plot(lambda x: np.arcsinh(x), **a)
        a8 = axes.plot(lambda x: np.arccosh(x), x_range=[+1, 6, 0.01])
        a9 = axes.plot(lambda x: -np.tanh(x), x_range=[-11, 11, 0.01]).rotate(PI/2).set_z_index(1)
        a10 = VGroup(
            axes.plot(lambda x: -1/np.sinh(x), x_range=[-11, -0.01, 0.01]),
            axes.plot(lambda x: -1/np.sinh(x), x_range=[+0.01, +11, 0.01]),
        ).rotate(PI/2).set_z_index(1)
        a11 = axes.plot(lambda x: 1/np.cosh(x), x_range=[-11, 0, 0.01])
        a11.rotate(-PI/2, about_point=[0, 0, 0]).set_z_index(1)
        a12 = VGroup(
            axes.plot(lambda x: -np.cosh(x)/np.sinh(x), x_range=[-11, -0.01, 0.01]),
            axes.plot(lambda x: -np.cosh(x)/np.sinh(x), x_range=[+0.01, +11, 0.01])
        ).rotate(PI/2).set_z_index(1)
        V = VGroup(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12)
        V.set_color_by_gradient([BLUE, PURPLE]).set_stroke(width=6)

        self.play(Create(axes))
        self.play(Create(a1), Write(sinh))
        self.wait()
        self.play(ReplacementTransform(a1, a2), ReplacementTransform(sinh, cosh))
        self.wait()
        self.play(ReplacementTransform(a2, a3), ReplacementTransform(cosh, tanh))
        self.wait()
        self.play(ReplacementTransform(a3, a4), ReplacementTransform(tanh, csch))
        self.wait()
        self.play(ReplacementTransform(a4, a5), ReplacementTransform(csch, sech))
        self.wait()
        self.play(ReplacementTransform(a5, a6), ReplacementTransform(sech, coth))
        self.wait()
        self.play(ReplacementTransform(a6, a7), ReplacementTransform(coth, arcsinh))
        self.wait()
        self.play(ReplacementTransform(a7, a8), ReplacementTransform(arcsinh, arccosh))
        self.wait()
        self.play(ReplacementTransform(a8, a9), ReplacementTransform(arccosh, arctanh))
        self.wait()
        self.play(ReplacementTransform(a9, a10), ReplacementTransform(arctanh, arccsch))
        self.wait()
        self.play(ReplacementTransform(a10, a11), ReplacementTransform(arccsch, arcsech))
        self.wait()
        self.play(ReplacementTransform(a11, a12), ReplacementTransform(arcsech, arccoth))
        self.wait()
        self.play(FadeOut(VGroup(axes, a12, arccoth)))
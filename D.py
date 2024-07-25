from manim import *
x = 50
config.frame_height = x
config.frame_width = 9*x/16
config.pixel_height = 1920*2
config.pixel_width = 1080*2

class khonggian(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60*DEGREES, theta=-60*DEGREES)
        #--------------------------------------------------------------------------------
        t1 = MathTex(r"0\text{D}").move_to(UP*15).scale(6)
        self.add_fixed_in_frame_mobjects(t1)
        self.wait(0.2)

        d0 = Dot3D(radius=0.05)
        d1 = Dot(radius=0)
        d2 = d1.copy()
        a1 = VGroup(d1, d2)

        l1 = always_redraw(lambda: Line(d1.get_center(), d2.get_center()).set_stroke(width=9))
                                                                                            #0D
        self.play(Write(VGroup(a1, l1, t1, d0)))

        t2 = MathTex(r"1\text{D}").move_to(UP*15).scale(6)
        self.remove(t1)
        self.add_fixed_in_frame_mobjects(t2)

        self.play(
            FadeOut(d0),
            VGroup(d1).animate.shift(LEFT*2), 
            VGroup(d2).animate.shift(-LEFT*2)                  #1D
        )
        #--------------------------------------------------------------------------------
        d3 = d1.copy()
        d4 = d2.copy()
        a2 = VGroup(d3, d4)

        l2 = always_redraw(lambda: Line(d1.get_center(), d3.get_center()).set_stroke(width=9))
        l3 = always_redraw(lambda: Line(d2.get_center(), d4.get_center()).set_stroke(width=9))
                                                                                            #2D
        i1 = l1.copy()
        self.add(a2, l2, l3)

        t3 = MathTex(r"2\text{D}").move_to(UP*15).scale(6)
        self.remove(t2)
        self.add_fixed_in_frame_mobjects(t3)

        self.play(
            VGroup(a1, l1).animate.shift(-UP*2), 
            VGroup(i1, a2).animate.shift(UP*2)
        )
        #--------------------------------------------------------------------------------
        d5 = d1.copy()
        d6 = d2.copy()
        d7 = d3.copy()
        d8 = d4.copy()
        a3 = VGroup(d5, d6, d7, d8)
                                                              
        l4 = always_redraw(lambda: Line(d1.get_center(), d5.get_center()).set_stroke(width=9)) 
        l5 = always_redraw(lambda: Line(d2.get_center(), d6.get_center()).set_stroke(width=9))              #3D
        l6 = always_redraw(lambda: Line(d3.get_center(), d7.get_center()).set_stroke(width=9))
        l7 = always_redraw(lambda: Line(d4.get_center(), d8.get_center()).set_stroke(width=9))

        i2 = VGroup(i1.copy(), l1, l2, l3).copy()
        self.add(a3, l4, l5, l6, l7)

        t4 = MathTex(r"3\text{D}").move_to(UP*15).scale(6)
        self.remove(t3)
        self.add_fixed_in_frame_mobjects(t4)

        self.play(
            VGroup(a3, i2).animate.shift(OUT*2), 
            VGroup(i1, l1, l2, l3, a1, a2).animate.shift(-OUT*2)
            )
        #--------------------------------------------------------------------------------
        d9  = d1.copy()
        d10 = d2.copy()
        d11 = d3.copy()
        d12 = d4.copy()
        d13 = d5.copy()
        d14 = d6.copy()
        d15 = d7.copy()
        d16 = d8.copy()
        a4 = VGroup(d9, d10, d11, d12, d13, d14, d15, d16)

        l8  = always_redraw(lambda: Line(d1.get_center(), d9.get_center()))
        l9  = always_redraw(lambda: Line(d2.get_center(), d10.get_center()))
        l10 = always_redraw(lambda: Line(d3.get_center(), d11.get_center()))
        l11 = always_redraw(lambda: Line(d4.get_center(), d12.get_center()))
        l12 = always_redraw(lambda: Line(d5.get_center(), d13.get_center()))
        l13 = always_redraw(lambda: Line(d6.get_center(), d14.get_center()))               #4D
        l14 = always_redraw(lambda: Line(d7.get_center(), d15.get_center()))
        l15 = always_redraw(lambda: Line(d8.get_center(), d16.get_center()))
        
        self.add(a4, l8, l9, l10, l11, l12, l13, l14, l15)
        i3 = VGroup(i2.copy(), l1, i1, l2, l3, l4, l5, l6, l7).copy()

        t5 = MathTex(r"4\text{D}").move_to(UP*15).scale(6)
        self.remove(t4)
        self.add_fixed_in_frame_mobjects(t5)

        self.play(
            VGroup(a4, i3).animate.shift(-2*LEFT+OUT+UP), 
            VGroup(i2, l1, i1, l2, l3, l4, l5, l6, l7, a1, a2, a3).animate.shift(2*LEFT-OUT-UP)
            )
        #--------------------------------------------------------------------------------
        d17 = d1.copy()
        d18 = d2.copy()
        d19 = d3.copy()
        d20 = d4.copy()
        d21 = d5.copy()
        d22 = d6.copy()
        d23 = d7.copy()
        d24 = d8.copy()
        d25 = d9.copy()
        d26 = d10.copy()
        d27 = d11.copy()
        d28 = d12.copy()
        d29 = d13.copy()
        d30 = d14.copy()
        d31 = d15.copy()
        d32 = d16.copy()

        a5 = VGroup(d17, d18, d19, d20, d21, d22, d23, d24, d25, d26, d27, d28, d29, d30, d31, d32)
        
        l16 = always_redraw(lambda: Line(d1.get_center(), d17.get_center()))
        l17 = always_redraw(lambda: Line(d2.get_center(), d18.get_center()))
        l18 = always_redraw(lambda: Line(d3.get_center(), d19.get_center()))
        l19 = always_redraw(lambda: Line(d4.get_center(), d20.get_center()))
        l20 = always_redraw(lambda: Line(d5.get_center(), d21.get_center()))
        l21 = always_redraw(lambda: Line(d6.get_center(), d22.get_center()))
        l22 = always_redraw(lambda: Line(d7.get_center(), d23.get_center()))
        l23 = always_redraw(lambda: Line(d8.get_center(), d24.get_center()))
        l24 = always_redraw(lambda: Line(d9.get_center(), d25.get_center()))
        l25 = always_redraw(lambda: Line(d10.get_center(), d26.get_center()))
        l26 = always_redraw(lambda: Line(d11.get_center(), d27.get_center()))
        l27 = always_redraw(lambda: Line(d12.get_center(), d28.get_center()))
        l28 = always_redraw(lambda: Line(d13.get_center(), d29.get_center()))
        l29 = always_redraw(lambda: Line(d14.get_center(), d30.get_center()))
        l30 = always_redraw(lambda: Line(d15.get_center(), d31.get_center()))
        l31 = always_redraw(lambda: Line(d16.get_center(), d32.get_center()))

        i4 = VGroup(
                i1, i2, i3.copy(),
                a1, a2, a3,
                l1,  l2,  l3,  l4,  l5, l6, l7, l8, l9, l10, 
                l11, l12, l13, l14, l15).copy()

        self.add(a5, l16, l17, l18, l19, l20, l21, l22, l23, l24, l25, l26, l27, l28, l29, l30, l31)

        t6 = MathTex(r"5\text{D}").move_to(UP*15).scale(6)
        self.remove(t5)
        self.add_fixed_in_frame_mobjects(t6)

        self.play(
            VGroup(a5, i4).animate.shift(2*UP+2*LEFT+OUT),
            VGroup(
                i1, i2, i3, 
                a1, a2, a3, a4,
                l1, l2, l3, l4, l5, l6, l7, a3, l8, l9, l10, 
                l11, l12, l13, l14, l15).animate.shift(-2*UP-2*LEFT-OUT)
            )
        #--------------------------------------------------------------------------------
        d33 = d1.copy()
        d34 = d2.copy()
        d35 = d3.copy()
        d36 = d4.copy()
        d37 = d5.copy()
        d38 = d6.copy()
        d39 = d7.copy()
        d40 = d8.copy()
        d41 = d9.copy()
        d42 = d10.copy()
        d43 = d11.copy()
        d44 = d12.copy()
        d45 = d13.copy()
        d46 = d14.copy()
        d47 = d15.copy()
        d48 = d16.copy()
        d49 = d17.copy()
        d50 = d18.copy()
        d51 = d19.copy()
        d52 = d20.copy()
        d53 = d21.copy()
        d54 = d22.copy()
        d55 = d23.copy()
        d56 = d24.copy()
        d57 = d25.copy()
        d58 = d26.copy()
        d59 = d27.copy()
        d60 = d28.copy()
        d61 = d29.copy()
        d62 = d30.copy()
        d63 = d31.copy()
        d64 = d32.copy()

        a6  =  VGroup(d33, d34, d35, d36, d37, d38, d39, d40, 
            d41, d42, d43, d44, d45, d46, d47, d48, d49, d50, 
            d51, d52, d53, d54, d55, d56, d57, d58, d59, d60, 
            d61, d62, d63, d64)

        l32 = always_redraw(lambda: Line(d1.get_center(), d33.get_center()))
        l33 = always_redraw(lambda: Line(d2.get_center(), d34.get_center()))
        l34 = always_redraw(lambda: Line(d3.get_center(), d35.get_center()))
        l35 = always_redraw(lambda: Line(d4.get_center(), d36.get_center()))
        l36 = always_redraw(lambda: Line(d5.get_center(), d37.get_center()))
        l37 = always_redraw(lambda: Line(d6.get_center(), d38.get_center()))
        l38 = always_redraw(lambda: Line(d7.get_center(), d39.get_center()))
        l39 = always_redraw(lambda: Line(d8.get_center(), d40.get_center()))
        l40 = always_redraw(lambda: Line(d9.get_center(), d41.get_center()))
        l41 = always_redraw(lambda: Line(d10.get_center(), d42.get_center()))
        l42 = always_redraw(lambda: Line(d11.get_center(), d43.get_center()))
        l43 = always_redraw(lambda: Line(d12.get_center(), d44.get_center()))
        l44 = always_redraw(lambda: Line(d13.get_center(), d45.get_center()))
        l45 = always_redraw(lambda: Line(d14.get_center(), d46.get_center()))
        l46 = always_redraw(lambda: Line(d15.get_center(), d47.get_center()))
        l47 = always_redraw(lambda: Line(d16.get_center(), d48.get_center()))
        l48 = always_redraw(lambda: Line(d17.get_center(), d49.get_center()))
        l49 = always_redraw(lambda: Line(d18.get_center(), d50.get_center()))
        l50 = always_redraw(lambda: Line(d19.get_center(), d51.get_center()))
        l51 = always_redraw(lambda: Line(d20.get_center(), d52.get_center()))
        l52 = always_redraw(lambda: Line(d21.get_center(), d53.get_center()))
        l53 = always_redraw(lambda: Line(d22.get_center(), d54.get_center()))
        l54 = always_redraw(lambda: Line(d23.get_center(), d55.get_center()))
        l55 = always_redraw(lambda: Line(d24.get_center(), d56.get_center()))
        l56 = always_redraw(lambda: Line(d25.get_center(), d57.get_center()))
        l57 = always_redraw(lambda: Line(d26.get_center(), d58.get_center()))
        l58 = always_redraw(lambda: Line(d27.get_center(), d59.get_center()))
        l59 = always_redraw(lambda: Line(d28.get_center(), d60.get_center()))
        l60 = always_redraw(lambda: Line(d29.get_center(), d61.get_center()))
        l61 = always_redraw(lambda: Line(d30.get_center(), d62.get_center()))
        l62 = always_redraw(lambda: Line(d31.get_center(), d63.get_center()))
        l63 = always_redraw(lambda: Line(d32.get_center(), d64.get_center()))

        i5 = VGroup(i4.copy(), 
            i1, i2, i3, 
            a1, a2, a3, a4, a5,
            l1,  l2,  l3,  l4,  l5,  l6,  l7,  l8,  l9,  l10, 
            l11, l12, l13, l14, l15, l16, l17, l18, l19, l20, 
            l21, l22, l23, l24, l25, l26, l27, l28, l29, l30, l31).copy()
        self.add(
            a6,  l32, l33, l34, l35, l36, l37, l38, l39, l40, 
            l41, l42, l43, l44, l45, l46, l47, l48, l49, l50, 
            l51, l52, l53, l54, l55, l56, l57, l58, l59, l60, 
            l61, l62, l63)

        t7 = MathTex(r"6\text{D}").move_to(UP*15).scale(6)
        self.remove(t6)
        self.add_fixed_in_frame_mobjects(t7)

        self.play(
            VGroup(a6, i5).animate.shift(-2*OUT-0.5*UP-3.5*LEFT),
            VGroup(
                i1, i2, i3, i4, 
                a1, a2, a3, a4, a5,
                l1,  l2,  l3,  l4,  l5,  l6,  l7,  l8,  l9,  l10, 
                l11, l12, l13, l14, l15, l16, l17, l18, l19, l20, 
                l21, l22, l23, l24, l25, l26, l27, l28, l29, l30, 
                l31).animate.shift(2*OUT+0.5*UP+3.5*LEFT)
            )
        #--------------------------------------------------------------------------------
        d65 = d1.copy()
        d66 = d2.copy()
        d67 = d3.copy()
        d68 = d4.copy()
        d69 = d5.copy()
        d70 = d6.copy()
        d71 = d7.copy()
        d72 = d8.copy()
        d73 = d9.copy()
        d74 = d10.copy()
        d75 = d11.copy()
        d76 = d12.copy()
        d77 = d13.copy()
        d78 = d14.copy()
        d79 = d15.copy()
        d80 = d16.copy()
        d81 = d17.copy()
        d82 = d18.copy()
        d83 = d19.copy()
        d84 = d20.copy()
        d85 = d21.copy()
        d86 = d22.copy()
        d87 = d23.copy()
        d88 = d24.copy()
        d89 = d25.copy()
        d90 = d26.copy()
        d91 = d27.copy()
        d92 = d28.copy()
        d93 = d29.copy()
        d94 = d30.copy()
        d95 = d31.copy()
        d96 = d32.copy()
        d97 = d33.copy()
        d98 = d34.copy()
        d99 = d35.copy()
        d100 = d36.copy()
        d101 = d37.copy()
        d102 = d38.copy()
        d103 = d39.copy()
        d104 = d40.copy()
        d105 = d41.copy()
        d106 = d42.copy()
        d107 = d43.copy()
        d108 = d44.copy()
        d109 = d45.copy()
        d110 = d46.copy()
        d111 = d47.copy()
        d112 = d48.copy()
        d113 = d49.copy()
        d114 = d50.copy()
        d115 = d51.copy()
        d116 = d52.copy()
        d117 = d53.copy()
        d118 = d54.copy()
        d119 = d55.copy()
        d120 = d56.copy()
        d121 = d57.copy()
        d122 = d58.copy()
        d123 = d59.copy()
        d124 = d60.copy()
        d125 = d61.copy()
        d126 = d62.copy()
        d127 = d63.copy()
        d128 = d64.copy()

        a7 = VGroup(                d65,  d66,  d67,  d68,  d69,  d70, 
            d71,  d72,  d73,  d74,  d75,  d76,  d77,  d78,  d79,  d80, 
            d81,  d82,  d83,  d84,  d85,  d86,  d87,  d88,  d89,  d90, 
            d91,  d92,  d93,  d94,  d95,  d96,  d97,  d98,  d99,  d100, 
            d101, d102, d103, d104, d105, d106, d107, d108, d109, d110, 
            d111, d112, d113, d114, d115, d116, d117, d118, d119, d120, 
            d121, d122, d123, d124, d125, d126, d127, d128)
        
        l64 = always_redraw(lambda: Line(d1.get_center(), d65.get_center()))
        l65 = always_redraw(lambda: Line(d2.get_center(), d66.get_center()))
        l66 = always_redraw(lambda: Line(d3.get_center(), d67.get_center()))
        l67 = always_redraw(lambda: Line(d4.get_center(), d68.get_center()))
        l68 = always_redraw(lambda: Line(d5.get_center(), d69.get_center()))
        l69 = always_redraw(lambda: Line(d6.get_center(), d70.get_center()))
        l70 = always_redraw(lambda: Line(d7.get_center(), d71.get_center()))
        l71 = always_redraw(lambda: Line(d8.get_center(), d72.get_center()))
        l72 = always_redraw(lambda: Line(d9.get_center(), d73.get_center()))
        l73 = always_redraw(lambda: Line(d10.get_center(), d74.get_center()))
        l74 = always_redraw(lambda: Line(d11.get_center(), d75.get_center()))
        l75 = always_redraw(lambda: Line(d12.get_center(), d76.get_center()))
        l76 = always_redraw(lambda: Line(d13.get_center(), d77.get_center()))
        l77 = always_redraw(lambda: Line(d14.get_center(), d78.get_center()))
        l78 = always_redraw(lambda: Line(d15.get_center(), d79.get_center()))
        l79 = always_redraw(lambda: Line(d16.get_center(), d80.get_center()))
        l80 = always_redraw(lambda: Line(d17.get_center(), d81.get_center()))
        l81 = always_redraw(lambda: Line(d18.get_center(), d82.get_center()))
        l82 = always_redraw(lambda: Line(d19.get_center(), d83.get_center()))
        l83 = always_redraw(lambda: Line(d20.get_center(), d84.get_center()))
        l84 = always_redraw(lambda: Line(d21.get_center(), d85.get_center()))
        l85 = always_redraw(lambda: Line(d22.get_center(), d86.get_center()))
        l86 = always_redraw(lambda: Line(d23.get_center(), d87.get_center()))
        l87 = always_redraw(lambda: Line(d24.get_center(), d88.get_center()))
        l88 = always_redraw(lambda: Line(d25.get_center(), d89.get_center()))
        l89 = always_redraw(lambda: Line(d26.get_center(), d90.get_center()))
        l90 = always_redraw(lambda: Line(d27.get_center(), d91.get_center()))
        l91 = always_redraw(lambda: Line(d28.get_center(), d92.get_center()))
        l92 = always_redraw(lambda: Line(d29.get_center(), d93.get_center()))
        l93 = always_redraw(lambda: Line(d30.get_center(), d94.get_center()))
        l94 = always_redraw(lambda: Line(d31.get_center(), d95.get_center()))
        l95 = always_redraw(lambda: Line(d32.get_center(), d96.get_center()))
        l96 = always_redraw(lambda: Line(d33.get_center(), d97.get_center()))
        l97 = always_redraw(lambda: Line(d34.get_center(), d98.get_center()))
        l98 = always_redraw(lambda: Line(d35.get_center(), d99.get_center()))
        l99 = always_redraw(lambda: Line(d36.get_center(), d100.get_center()))
        l100 = always_redraw(lambda: Line(d37.get_center(), d101.get_center()))
        l101 = always_redraw(lambda: Line(d38.get_center(), d102.get_center()))
        l102 = always_redraw(lambda: Line(d39.get_center(), d103.get_center()))
        l103 = always_redraw(lambda: Line(d40.get_center(), d104.get_center()))
        l104 = always_redraw(lambda: Line(d41.get_center(), d105.get_center()))
        l105 = always_redraw(lambda: Line(d42.get_center(), d106.get_center()))
        l106 = always_redraw(lambda: Line(d43.get_center(), d107.get_center()))
        l107 = always_redraw(lambda: Line(d44.get_center(), d108.get_center()))
        l108 = always_redraw(lambda: Line(d45.get_center(), d109.get_center()))
        l109 = always_redraw(lambda: Line(d46.get_center(), d110.get_center()))
        l110 = always_redraw(lambda: Line(d47.get_center(), d111.get_center()))
        l111 = always_redraw(lambda: Line(d48.get_center(), d112.get_center()))
        l112 = always_redraw(lambda: Line(d49.get_center(), d113.get_center()))
        l113 = always_redraw(lambda: Line(d50.get_center(), d114.get_center()))
        l114 = always_redraw(lambda: Line(d51.get_center(), d115.get_center()))
        l115 = always_redraw(lambda: Line(d52.get_center(), d116.get_center()))
        l116 = always_redraw(lambda: Line(d53.get_center(), d117.get_center()))
        l117 = always_redraw(lambda: Line(d54.get_center(), d118.get_center()))
        l118 = always_redraw(lambda: Line(d55.get_center(), d119.get_center()))
        l119 = always_redraw(lambda: Line(d56.get_center(), d120.get_center()))
        l120 = always_redraw(lambda: Line(d57.get_center(), d121.get_center()))
        l121 = always_redraw(lambda: Line(d58.get_center(), d122.get_center()))
        l122 = always_redraw(lambda: Line(d59.get_center(), d123.get_center()))
        l123 = always_redraw(lambda: Line(d60.get_center(), d124.get_center()))
        l124 = always_redraw(lambda: Line(d61.get_center(), d125.get_center()))
        l125 = always_redraw(lambda: Line(d62.get_center(), d126.get_center()))
        l126 = always_redraw(lambda: Line(d63.get_center(), d127.get_center()))
        l127 = always_redraw(lambda: Line(d64.get_center(), d128.get_center()))

        i6 = VGroup(i5.copy(),
            i4, i3, i2, i1,

            a1, a2, a3, a4, a5, a6,

            l1,  l2,  l3,  l4,  l5,  l6,  l7,  l8,  l9,  l10, 
            l11, l12, l13, l14, l15, l16, l17, l18, l19, l20, 
            l21, l22, l23, l24, l25, l26, l27, l28, l29, l30, 
            l31, l32, l33, l34, l35, l36, l37, l38, l39, l40, 
            l41, l42, l43, l44, l45, l46, l47, l48, l49, l50,
            l51, l52, l53, l54, l55, l56, l57, l58, l59, l60, 
            l61, l62, l63).copy()

        self.add(a7,          l64,  l65,  l66,  l67,  l68,  l69,  l70, 
            l71,  l72,  l73,  l74,  l75,  l76,  l77,  l78,  l79,  l80, 
            l81,  l82,  l83,  l84,  l85,  l86,  l87,  l88,  l89,  l90, 
            l91,  l92,  l93,  l94,  l95,  l96,  l97,  l98,  l99,  l100, 
            l101, l102, l103, l104, l105, l106, l107, l108, l109, l110, 
            l111, l112, l113, l114, l115, l116, l117, l118, l119, l120, 
            l121, l122, l123, l124, l125, l126, l127)

        t8 = MathTex(r"7\text{D}").move_to(UP*15).scale(6)
        self.remove(t7)
        self.add_fixed_in_frame_mobjects(t8)

        self.play(
            VGroup(a7, i6).animate.shift(3*OUT+3*UP-LEFT),
            VGroup(
                i1, i2, i3, i4, i5, 
                a1, a2, a3, a4, a5, a6,
                l1,  l2,  l3,  l4,  l5,  l6,  l7,  l8,  l9,  l10, 
                l11, l12, l13, l14, l15, l16, l17, l18, l19, l20, 
                l21, l22, l23, l24, l25, l26, l27, l28, l29, l30, 
                l31, l32, l33, l34, l35, l36, l37, l38, l39, l40, 
                l41, l42, l43, l44, l45, l46, l47, l48, l49, l50, 
                l51, l52, l53, l54, l55, l56, l57, l58, l59, l60,
                l61, l62, l63).animate.shift(-3*OUT-3*UP+LEFT)
            )
        

        #self.move_camera(phi=60 * DEGREES, theta=360*2*DEGREES, run_time=10)
        d129 = d1.copy()
        d130 = d2.copy()
        d131 = d3.copy()
        d132 = d4.copy()
        d133 = d5.copy()
        d134 = d6.copy()
        d135 = d7.copy()
        d136 = d8.copy()
        d137 = d9.copy()
        d138 = d10.copy()
        d139 = d11.copy()
        d140 = d12.copy()
        d141 = d13.copy()
        d142 = d14.copy()
        d143 = d15.copy()
        d144 = d16.copy()
        d145 = d17.copy()
        d146 = d18.copy()
        d147 = d19.copy()
        d148 = d20.copy()
        d149 = d21.copy()
        d150 = d22.copy()
        d151 = d23.copy()
        d152 = d24.copy()
        d153 = d25.copy()
        d154 = d26.copy()
        d155 = d27.copy()
        d156 = d28.copy()
        d157 = d29.copy()
        d158 = d30.copy()
        d159 = d31.copy()
        d160 = d32.copy()
        d161 = d33.copy()
        d162 = d34.copy()
        d163 = d35.copy()
        d164 = d36.copy()
        d165 = d37.copy()
        d166 = d38.copy()
        d167 = d39.copy()
        d168 = d40.copy()
        d169 = d41.copy()
        d170 = d42.copy()
        d171 = d43.copy()
        d172 = d44.copy()
        d173 = d45.copy()
        d174 = d46.copy()
        d175 = d47.copy()
        d176 = d48.copy()
        d177 = d49.copy()
        d178 = d50.copy()
        d179 = d51.copy()
        d180 = d52.copy()
        d181 = d53.copy()
        d182 = d54.copy()
        d183 = d55.copy()
        d184 = d56.copy()
        d185 = d57.copy()
        d186 = d58.copy()
        d187 = d59.copy()
        d188 = d60.copy()
        d189 = d61.copy()
        d190 = d62.copy()
        d191 = d63.copy()
        d192 = d64.copy()
        d193 = d65.copy()
        d194 = d66.copy()
        d195 = d67.copy()
        d196 = d68.copy()
        d197 = d69.copy()
        d198 = d70.copy()
        d199 = d71.copy()
        d200 = d72.copy()
        d201 = d73.copy()
        d202 = d74.copy()
        d203 = d75.copy()
        d204 = d76.copy()
        d205 = d77.copy()
        d206 = d78.copy()
        d207 = d79.copy()
        d208 = d80.copy()
        d209 = d81.copy()
        d210 = d82.copy()
        d211 = d83.copy()
        d212 = d84.copy()
        d213 = d85.copy()
        d214 = d86.copy()
        d215 = d87.copy()
        d216 = d88.copy()
        d217 = d89.copy()
        d218 = d90.copy()
        d219 = d91.copy()
        d220 = d92.copy()
        d221 = d93.copy()
        d222 = d94.copy()
        d223 = d95.copy()
        d224 = d96.copy()
        d225 = d97.copy()
        d226 = d98.copy()
        d227 = d99.copy()
        d228 = d100.copy()
        d229 = d101.copy()
        d230 = d102.copy()
        d231 = d103.copy()
        d232 = d104.copy()
        d233 = d105.copy()
        d234 = d106.copy()
        d235 = d107.copy()
        d236 = d108.copy()
        d237 = d109.copy()
        d238 = d110.copy()
        d239 = d111.copy()
        d240 = d112.copy()
        d241 = d113.copy()
        d242 = d114.copy()
        d243 = d115.copy()
        d244 = d116.copy()
        d245 = d117.copy()
        d246 = d118.copy()
        d247 = d119.copy()
        d248 = d120.copy()
        d249 = d121.copy()
        d250 = d122.copy()
        d251 = d123.copy()
        d252 = d124.copy()
        d253 = d125.copy()
        d254 = d126.copy()
        d255 = d127.copy()
        d256 = d128.copy()
        a8 = VGroup(d129, d130,
            d131, d132, d133, d134, d135, d136, d137, d138, d139, d140, 
            d141, d142, d143, d144, d145, d146, d147, d148, d149, d150, 
            d151, d152, d153, d154, d155, d156, d157, d158, d159, d160, 
            d161, d162, d163, d164, d165, d166, d167, d168, d169, d170, 
            d171, d172, d173, d174, d175, d176, d177, d178, d179, d180, 
            d181, d182, d183, d184, d185, d186, d187, d188, d189, d190, 
            d191, d192, d193, d194, d195, d196, d197, d198, d199, d200, 
            d201, d202, d203, d204, d205, d206, d207, d208, d209, d210, 
            d211, d212, d213, d214, d215, d216, d217, d218, d219, d220, 
            d221, d222, d223, d224, d225, d226, d227, d228, d229, d230, 
            d231, d232, d233, d234, d235, d236, d237, d238, d239, d240, 
            d241, d242, d243, d244, d245, d246, d247, d248, d249, d250, 
            d251, d252, d253, d254, d255, d256)

        l128 = always_redraw(lambda: Line(d1.get_center(), d129.get_center()))
        l129 = always_redraw(lambda: Line(d2.get_center(), d130.get_center()))
        l130 = always_redraw(lambda: Line(d3.get_center(), d131.get_center()))
        l131 = always_redraw(lambda: Line(d4.get_center(), d132.get_center()))
        l132 = always_redraw(lambda: Line(d5.get_center(), d133.get_center()))
        l133 = always_redraw(lambda: Line(d6.get_center(), d134.get_center()))
        l134 = always_redraw(lambda: Line(d7.get_center(), d135.get_center()))
        l135 = always_redraw(lambda: Line(d8.get_center(), d136.get_center()))
        l136 = always_redraw(lambda: Line(d9.get_center(), d137.get_center()))
        l137 = always_redraw(lambda: Line(d10.get_center(), d138.get_center()))
        l138 = always_redraw(lambda: Line(d11.get_center(), d139.get_center()))
        l139 = always_redraw(lambda: Line(d12.get_center(), d140.get_center()))
        l140 = always_redraw(lambda: Line(d13.get_center(), d141.get_center()))
        l141 = always_redraw(lambda: Line(d14.get_center(), d142.get_center()))
        l142 = always_redraw(lambda: Line(d15.get_center(), d143.get_center()))
        l143 = always_redraw(lambda: Line(d16.get_center(), d144.get_center()))
        l144 = always_redraw(lambda: Line(d17.get_center(), d145.get_center()))
        l145 = always_redraw(lambda: Line(d18.get_center(), d146.get_center()))
        l146 = always_redraw(lambda: Line(d19.get_center(), d147.get_center()))
        l147 = always_redraw(lambda: Line(d20.get_center(), d148.get_center()))
        l148 = always_redraw(lambda: Line(d21.get_center(), d149.get_center()))
        l149 = always_redraw(lambda: Line(d22.get_center(), d150.get_center()))
        l150 = always_redraw(lambda: Line(d23.get_center(), d151.get_center()))
        l151 = always_redraw(lambda: Line(d24.get_center(), d152.get_center()))
        l152 = always_redraw(lambda: Line(d25.get_center(), d153.get_center()))
        l153 = always_redraw(lambda: Line(d26.get_center(), d154.get_center()))
        l154 = always_redraw(lambda: Line(d27.get_center(), d155.get_center()))
        l155 = always_redraw(lambda: Line(d28.get_center(), d156.get_center()))
        l156 = always_redraw(lambda: Line(d29.get_center(), d157.get_center()))
        l157 = always_redraw(lambda: Line(d30.get_center(), d158.get_center()))
        l158 = always_redraw(lambda: Line(d31.get_center(), d159.get_center()))
        l159 = always_redraw(lambda: Line(d32.get_center(), d160.get_center()))
        l160 = always_redraw(lambda: Line(d33.get_center(), d161.get_center()))
        l161 = always_redraw(lambda: Line(d34.get_center(), d162.get_center()))
        l162 = always_redraw(lambda: Line(d35.get_center(), d163.get_center()))
        l163 = always_redraw(lambda: Line(d36.get_center(), d164.get_center()))
        l164 = always_redraw(lambda: Line(d37.get_center(), d165.get_center()))
        l165 = always_redraw(lambda: Line(d38.get_center(), d166.get_center()))
        l166 = always_redraw(lambda: Line(d39.get_center(), d167.get_center()))
        l167 = always_redraw(lambda: Line(d40.get_center(), d168.get_center()))
        l168 = always_redraw(lambda: Line(d41.get_center(), d169.get_center()))
        l169 = always_redraw(lambda: Line(d42.get_center(), d170.get_center()))
        l170 = always_redraw(lambda: Line(d43.get_center(), d171.get_center()))
        l171 = always_redraw(lambda: Line(d44.get_center(), d172.get_center()))
        l172 = always_redraw(lambda: Line(d45.get_center(), d173.get_center()))
        l173 = always_redraw(lambda: Line(d46.get_center(), d174.get_center()))
        l174 = always_redraw(lambda: Line(d47.get_center(), d175.get_center()))
        l175 = always_redraw(lambda: Line(d48.get_center(), d176.get_center()))
        l176 = always_redraw(lambda: Line(d49.get_center(), d177.get_center()))
        l177 = always_redraw(lambda: Line(d50.get_center(), d178.get_center()))
        l178 = always_redraw(lambda: Line(d51.get_center(), d179.get_center()))
        l179 = always_redraw(lambda: Line(d52.get_center(), d180.get_center()))
        l180 = always_redraw(lambda: Line(d53.get_center(), d181.get_center()))
        l181 = always_redraw(lambda: Line(d54.get_center(), d182.get_center()))
        l182 = always_redraw(lambda: Line(d55.get_center(), d183.get_center()))
        l183 = always_redraw(lambda: Line(d56.get_center(), d184.get_center()))
        l184 = always_redraw(lambda: Line(d57.get_center(), d185.get_center()))
        l185 = always_redraw(lambda: Line(d58.get_center(), d186.get_center()))
        l186 = always_redraw(lambda: Line(d59.get_center(), d187.get_center()))
        l187 = always_redraw(lambda: Line(d60.get_center(), d188.get_center()))
        l188 = always_redraw(lambda: Line(d61.get_center(), d189.get_center()))
        l189 = always_redraw(lambda: Line(d62.get_center(), d190.get_center()))
        l190 = always_redraw(lambda: Line(d63.get_center(), d191.get_center()))
        l191 = always_redraw(lambda: Line(d64.get_center(), d192.get_center()))
        l192 = always_redraw(lambda: Line(d65.get_center(), d193.get_center()))
        l193 = always_redraw(lambda: Line(d66.get_center(), d194.get_center()))
        l194 = always_redraw(lambda: Line(d67.get_center(), d195.get_center()))
        l195 = always_redraw(lambda: Line(d68.get_center(), d196.get_center()))
        l196 = always_redraw(lambda: Line(d69.get_center(), d197.get_center()))
        l197 = always_redraw(lambda: Line(d70.get_center(), d198.get_center()))
        l198 = always_redraw(lambda: Line(d71.get_center(), d199.get_center()))
        l199 = always_redraw(lambda: Line(d72.get_center(), d200.get_center()))
        l200 = always_redraw(lambda: Line(d73.get_center(), d201.get_center()))
        l201 = always_redraw(lambda: Line(d74.get_center(), d202.get_center()))
        l202 = always_redraw(lambda: Line(d75.get_center(), d203.get_center()))
        l203 = always_redraw(lambda: Line(d76.get_center(), d204.get_center()))
        l204 = always_redraw(lambda: Line(d77.get_center(), d205.get_center()))
        l205 = always_redraw(lambda: Line(d78.get_center(), d206.get_center()))
        l206 = always_redraw(lambda: Line(d79.get_center(), d207.get_center()))
        l207 = always_redraw(lambda: Line(d80.get_center(), d208.get_center()))
        l208 = always_redraw(lambda: Line(d81.get_center(), d209.get_center()))
        l209 = always_redraw(lambda: Line(d82.get_center(), d210.get_center()))
        l210 = always_redraw(lambda: Line(d83.get_center(), d211.get_center()))
        l211 = always_redraw(lambda: Line(d84.get_center(), d212.get_center()))
        l212 = always_redraw(lambda: Line(d85.get_center(), d213.get_center()))
        l213 = always_redraw(lambda: Line(d86.get_center(), d214.get_center()))
        l214 = always_redraw(lambda: Line(d87.get_center(), d215.get_center()))
        l215 = always_redraw(lambda: Line(d88.get_center(), d216.get_center()))
        l216 = always_redraw(lambda: Line(d89.get_center(), d217.get_center()))
        l217 = always_redraw(lambda: Line(d90.get_center(), d218.get_center()))
        l218 = always_redraw(lambda: Line(d91.get_center(), d219.get_center()))
        l219 = always_redraw(lambda: Line(d92.get_center(), d220.get_center()))
        l220 = always_redraw(lambda: Line(d93.get_center(), d221.get_center()))
        l221 = always_redraw(lambda: Line(d94.get_center(), d222.get_center()))
        l222 = always_redraw(lambda: Line(d95.get_center(), d223.get_center()))
        l223 = always_redraw(lambda: Line(d96.get_center(), d224.get_center()))
        l224 = always_redraw(lambda: Line(d97.get_center(), d225.get_center()))
        l225 = always_redraw(lambda: Line(d98.get_center(), d226.get_center()))
        l226 = always_redraw(lambda: Line(d99.get_center(), d227.get_center()))
        l227 = always_redraw(lambda: Line(d100.get_center(), d228.get_center()))
        l228 = always_redraw(lambda: Line(d101.get_center(), d229.get_center()))
        l229 = always_redraw(lambda: Line(d102.get_center(), d230.get_center()))
        l230 = always_redraw(lambda: Line(d103.get_center(), d231.get_center()))
        l231 = always_redraw(lambda: Line(d104.get_center(), d232.get_center()))
        l232 = always_redraw(lambda: Line(d105.get_center(), d233.get_center()))
        l233 = always_redraw(lambda: Line(d106.get_center(), d234.get_center()))
        l234 = always_redraw(lambda: Line(d107.get_center(), d235.get_center()))
        l235 = always_redraw(lambda: Line(d108.get_center(), d236.get_center()))
        l236 = always_redraw(lambda: Line(d109.get_center(), d237.get_center()))
        l237 = always_redraw(lambda: Line(d110.get_center(), d238.get_center()))
        l238 = always_redraw(lambda: Line(d111.get_center(), d239.get_center()))
        l239 = always_redraw(lambda: Line(d112.get_center(), d240.get_center()))
        l240 = always_redraw(lambda: Line(d113.get_center(), d241.get_center()))
        l241 = always_redraw(lambda: Line(d114.get_center(), d242.get_center()))
        l242 = always_redraw(lambda: Line(d115.get_center(), d243.get_center()))
        l243 = always_redraw(lambda: Line(d116.get_center(), d244.get_center()))
        l244 = always_redraw(lambda: Line(d117.get_center(), d245.get_center()))
        l245 = always_redraw(lambda: Line(d118.get_center(), d246.get_center()))
        l246 = always_redraw(lambda: Line(d119.get_center(), d247.get_center()))
        l247 = always_redraw(lambda: Line(d120.get_center(), d248.get_center()))
        l248 = always_redraw(lambda: Line(d121.get_center(), d249.get_center()))
        l249 = always_redraw(lambda: Line(d122.get_center(), d250.get_center()))
        l250 = always_redraw(lambda: Line(d123.get_center(), d251.get_center()))
        l251 = always_redraw(lambda: Line(d124.get_center(), d252.get_center()))
        l252 = always_redraw(lambda: Line(d125.get_center(), d253.get_center()))
        l253 = always_redraw(lambda: Line(d126.get_center(), d254.get_center()))
        l254 = always_redraw(lambda: Line(d127.get_center(), d255.get_center()))
        l255 = always_redraw(lambda: Line(d128.get_center(), d256.get_center()))
        i7 = VGroup(
            i6.copy(), i5, i4, i3, i2, i1,
            a1, a2, a3, a4, a5, a6, a7,
            l1,   l2,   l3,   l4,   l5,   l6,   l7,   l8,   l9,   l10, 
            l11,  l12,  l13,  l14,  l15,  l16,  l17,  l18,  l19,  l20, 
            l21,  l22,  l23,  l24,  l25,  l26,  l27,  l28,  l29,  l30,
            l31,  l32,  l33,  l34,  l35,  l36,  l37,  l38,  l39,  l40, 
            l41,  l42,  l43,  l44,  l45,  l46,  l47,  l48,  l49,  l50, 
            l51,  l52,  l53,  l54,  l55,  l56,  l57,  l58,  l59,  l60, 
            l61,  l62,  l63,  l64,  l65,  l66,  l67,  l68,  l69,  l70, 
            l71,  l72,  l73,  l74,  l75,  l76,  l77,  l78,  l79,  l80, 
            l81,  l82,  l83,  l84,  l85,  l86,  l87,  l88,  l89,  l90, 
            l91,  l92,  l93,  l94,  l95,  l96,  l97,  l98,  l99,  l100, 
            l101, l102, l103, l104, l105, l106, l107, l108, l109, l110, 
            l111, l112, l113, l114, l115, l116, l117, l118, l119, l120, 
            l121, l122, l123, l124, l125, l126, l127).copy()

        self.add(a8, l128, l129, l130, 
            l131, l132, l133, l134, l135, l136, l137, l138, l139, l140, 
            l141, l142, l143, l144, l145, l146, l147, l148, l149, l150, 
            l151, l152, l153, l154, l155, l156, l157, l158, l159, l160, 
            l161, l162, l163, l164, l165, l166, l167, l168, l169, l170, 
            l171, l172, l173, l174, l175, l176, l177, l178, l179, l180, 
            l181, l182, l183, l184, l185, l186, l187, l188, l189, l190, 
            l191, l192, l193, l194, l195, l196, l197, l198, l199, l200, 
            l201, l202, l203, l204, l205, l206, l207, l208, l209, l210, 
            l211, l212, l213, l214, l215, l216, l217, l218, l219, l220, 
            l221, l222, l223, l224, l225, l226, l227, l228, l229, l230, 
            l231, l232, l233, l234, l235, l236, l237, l238, l239, l240, 
            l241, l242, l243, l244, l245, l246, l247, l248, l249, l250, 
            l251, l252, l253, l254, l255)

        t9 = MathTex(r"8\text{D}").move_to(UP*15).scale(6)
        self.remove(t8)
        self.add_fixed_in_frame_mobjects(t9)
        self.play(
            VGroup(a8, i7).animate.shift(0.5*OUT-4*UP+2*LEFT),
            VGroup(
                i1, i2, i3, i4, i5, i6, 
                a1, a2, a3, a4, a5, a6, a7,
                l1,   l2,   l3,   l4,   l5,   l6,   l7,   l8,   l9,   l10, 
                l11,  l12,  l13,  l14,  l15,  l16,  l17,  l18,  l19,  l20, 
                l21,  l22,  l23,  l24,  l25,  l26,  l27,  l28,  l29,  l30,
                l31,  l32,  l33,  l34,  l35,  l36,  l37,  l38,  l39,  l40, 
                l41,  l42,  l43,  l44,  l45,  l46,  l47,  l48,  l49,  l50, 
                l51,  l52,  l53,  l54,  l55,  l56,  l57,  l58,  l59,  l60, 
                l61,  l62,  l63,  l64,  l65,  l66,  l67,  l68,  l69,  l70, 
                l71,  l72,  l73,  l74,  l75,  l76,  l77,  l78,  l79,  l80, 
                l81,  l82,  l83,  l84,  l85,  l86,  l87,  l88,  l89,  l90, 
                l91,  l92,  l93,  l94,  l95,  l96,  l97,  l98,  l99,  l100, 
                l101, l102, l103, l104, l105, l106, l107, l108, l109, l110, 
                l111, l112, l113, l114, l115, l116, l117, l118, l119, l120, 
                l121, l122, l123, l124, l125, l126, l127).animate.shift(-0.5*OUT+4*UP-2*LEFT)
            )
        self.move_camera(phi=60 * DEGREES, theta=300*DEGREES, run_time=10)
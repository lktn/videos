from manim import *
from skimage.measure import marching_cubes

config.pixel_height = 2880
config.pixel_width = 1620

def ImplicitSurface(f, x_range, y_range, z_range, axes):
    X, Y, Z = np.mgrid[
        x_range[0]:x_range[1]:x_range[2]*1j,
        y_range[0]:y_range[1]:y_range[2]*1j,
        z_range[0]:z_range[1]:z_range[2]*1j
    ]

    dx = (x_range[1] - x_range[0]) / (x_range[2] - 1)
    dy = (y_range[1] - y_range[0]) / (y_range[2] - 1)
    dz = (z_range[1] - z_range[0]) / (z_range[2] - 1)

    verts, faces, _, _ = marching_cubes(f(X, Y, Z), level=0, spacing=(dx, dy, dz))

    verts[:, 0] += x_range[0]
    verts[:, 1] += y_range[0]
    verts[:, 2] += z_range[0]

    return VGroup(*[
        Polygon(
            *[axes.c2p(*p) for p in verts[i]],
            fill_opacity=1,
            stroke_width=0.7
        )
        for i in faces
    ]).set_shade_in_3d(True)

class HeartEquation(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=-60 * DEGREES)
        axes = ThreeDAxes(
            x_range=[-1.7, 1.7, 0.34],
            y_range=[-1.7, 1.7, 0.34],
            z_range=[-1.7, 1.7, 0.34],
            x_length=12,
            y_length=12,
            z_length=12,
            tips=False
        )

        axes.move_to(OUT)
        axes.x_axis.set_stroke(width=3)
        axes.y_axis.set_stroke(width=3)
        axes.z_axis.set_stroke(width=3)
        self.add(axes)

        text = VGroup(
            Tex(r"3D Heart Equation").scale(2.3).move_to(6*DOWN).set_color_by_gradient(RED, PINK),
            MathTex(r"4(x^2 + 2y^2 + z^2 - 1)^3 = 7x^2z^3 + y^2z^3").scale(1.3).move_to(7.5*DOWN)
        )
        self.add_fixed_in_frame_mobjects(text)
        self.wait(0.3)

        heart = ImplicitSurface(
            lambda x, y, z: 4*(x**2 + 2*y**2 + z**2 - 1)**3 - 7*x**2*z**3 - y**2*z**3,
            x_range=[-1.22, 1.22, 70],
            y_range=[-0.73, 0.73, 70],
            z_range=[-1, 1.34, 70],
            axes=axes
        ).set_color_by_gradient(RED, PINK)

        self.play(GrowFromCenter(heart))
        self.move_camera(phi=65*DEGREES, theta=300*DEGREES, run_time=8)
        self.wait(0.5)
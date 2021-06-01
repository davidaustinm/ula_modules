def q(r, theta):
    v = vector([r*cos(theta), r*sin(theta)])
    return v * (A*v)

def quad_plot(A):
    r, theta, z = var('r theta z')    
    T = Cylindrical('height', ['radius', 'azimuth'])
    T.transform(radius = r, azimuth = theta, height = z)
    graph = plot3d(q(r, theta), (r, 0, 2), (theta, 0, 2*pi),
                   color='orange', opacity=0.9,
	           aspect_ratio=(1,1,1/max(matrix(RDF,A).singular_values())),
	           transformation=T)
    curve = parametric_plot3d([cos(theta), sin(theta), q(1, theta)],
                              (theta,0,2*pi), thickness=3)
    return graph + curve

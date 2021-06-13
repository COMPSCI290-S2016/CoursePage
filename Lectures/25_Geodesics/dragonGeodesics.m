addpath(genpath('toolbox_fast_marching'));
[vertex, faces] = read_mesh('dragon.off');

start_points = 1;
options.blah = 0;
[D,S,Q] = perform_fast_marching_mesh(vertex, faces, start_points, options);
end_points = 200;
options.v2v = compute_vertex_ring(faces);
options.e2f = compute_edge_face_ring(faces);
options.method = 'continuous';
options.verb = 0;
paths = compute_geodesic_mesh(D,vertex,faces, end_points, options);

options.colorfx = 'equalize';
plot_fast_marching_mesh(vertex,faces, D, paths, options);
shading interp;
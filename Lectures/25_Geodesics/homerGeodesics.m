addpath(genpath('toolbox_fast_marching'));
[vertex, faces] = read_mesh('homer.off');
lfinger = 31;
rfinger = 41;
nose = 847;
beard = 805;

start_points = beard;
options.blah = 0;
[D,S,Q] = perform_fast_marching_mesh(vertex, faces, start_points, options);
end_points = lfinger;
options.v2v = compute_vertex_ring(faces);
options.e2f = compute_edge_face_ring(faces);
options.method = 'continuous';
options.verb = 0;
paths = compute_geodesic_mesh(D,vertex,faces, end_points, options);

options.colorfx = 'equalize';
plot_fast_marching_mesh(vertex,faces, D, paths, options);
shading interp;
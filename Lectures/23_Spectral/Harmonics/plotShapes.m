addpath('toolbox_fast_marching');
addpath('toolbox_fast_marching/toolbox');
addpath('toolbox_fast_marching/data');

for ii = 0:20
    clf;
    [vertex, faces, color] = readColorOff(sprintf('HomerModes/homer%i.off', ii));
    plot_fast_marching_mesh(vertex', faces', color'/255.0, [])
    shading interp;
    print('-dpng', '-r100', sprintf('HomerModes/%i.png', ii));
end

for ii = 0:20
    clf;
    [vertex, faces, color] = readColorOff(sprintf('CheetahModes/cheetah%i.off', ii));
    V = vertex([2, 3, 1], :);
    plot_fast_marching_mesh(V', faces', color'/255.0, []);
    view(90, -90);
    shading interp;
    print('-dpng', '-r100', sprintf('CheetahModes/%i.png', ii));
end
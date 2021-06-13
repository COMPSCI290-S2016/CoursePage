addpath('../25_Geodesics/toolbox_fast_marching');
addpath('../25_Geodesics/toolbox_fast_marching/toolbox');
addpath('../25_Geodesics/toolbox_fast_marching/data');

% [vertexChris, facesChris] = read_mesh('chris.off');
% N = size(vertexChris, 2);
% D = zeros(N, N);
% for ii = 1:N
%    D(ii, :) = perform_fast_marching_mesh(vertexChris, facesChris, ii);
%    fprintf(1, '.');
%    if mod(ii, 50) == 0
%       fprintf(1, '\n'); 
%    end
% end
% D = D( [1:414 416:end], [1:414 416:end] );
% [vertexChrisCanon, eigsChris] = cmdscale(0.5*(D + D'));
% vertexChrisCanon = vertexChrisCanon(:, 1:3);
% vertexChrisCanon = [vertexChrisCanon(1:414, :) ; 0 0 0 ; vertexChrisCanon(415:end, :)];


% [vertexCamel, facesCamel] = read_mesh('camel.off');
% N = size(vertexCamel, 2);
% D = zeros(N, N);
for ii = 15454:N
   D(ii, :) = perform_fast_marching_mesh(vertexCamel, facesCamel, ii);
   fprintf(1, '.');
   if mod(ii, 50) == 0
      fprintf(1, '\n'); 
   end
end
[vertexCamelCanon, eigsCamel] = cmdscale(0.5*(D + D'));
vertexCamelCanon = vertexCamelCanon(:, 1:3);

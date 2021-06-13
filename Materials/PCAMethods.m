%Programmer: Chris Tralie
%Purpose: To Illustrate 4 Different Ways To Do PCA in Matlab
rng(100);
dim = 3;
%Make a random point cloud
X = randn(1000, 3);
%Apply a scale to each dimension
X = bsxfun(@times, rand(1, dim), X);

%Apply a random rotation
%Make a random rotation matrix
R = randn(3, 3);
[R, ~, ~] = svd(R);
X = X*R;

%Apply a random translation
X = bsxfun(@plus, randn(1, dim), X);
plot3(X(:, 1), X(:, 2), X(:, 3), '.');
axis equal;

%Do PCA 4 different ways!
%1) The SVD way
Y = bsxfun(@minus, mean(X, 1), X); %Subtract off the mean
[Usvd, S, Vsvd] = svd(Y);
%Principal components lie in V (along columns!)
%Variances lie along diagonal of S

%2) Explicity eigenvector way
%NOTE: This sorts them from small to big!
YtY = Y'*Y;
[Vdirect, Vdirecteigs] = eig(YtY);
%YProjDirect is the point cloud in a coordinate system where each
%coordinate axis is a principal direction (found in the columns of Vdirect)
YProjDirect = Y*Vdirect; %Because each point is a row vector!  
%This is actually the inverse rotation matrix pulling me back to PCA's coordinate system

%3) Matlab's builtin command
%XProj is the same exact thing as as YProjDirect becuase mean-centering is
%built into the pca command.
[V, XProj, latent] = pca(X);

%4) Classic multidimensional scaling after pdist2
D = pdist2(X, X);
[YProjpdist, latentpdist] = cmdscale(D);

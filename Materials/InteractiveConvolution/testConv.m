[X, Fs] = audioread('blair.wav');
[Y, Fs] = audioread('barry.wav');
ZGT = conv(X, Y);

M = length(X);
N = length(Y);
X = [X(:); zeros(N+1, 1)];
Y = [Y(:); zeros(M+1, 1)];

Z = fft(X).*fft(Y);
Z = ifft(Z);
Z = Z/max(abs(Z));
sound(Z, Fs);
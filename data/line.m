[X,Y]=meshgrid(-2:0.0125:2,-2:0.0125:2);
[n,m]=size(X);
z=zeros(size(X));
for i=1:n
    for j=1:m
        xx=X(i,j);
        yy=Y(i,j);
        if(xx*xx + yy * yy < 0.05)
            z(i,j)=1;
        end
    end
end
figure;
imshow(z)
imwrite(z, 'slit.png')

Z=fft2(z);
ZZ=abs(fftshift(Z)).^2;
figure; surfl(ZZ); shading flat; colormap(gray);

ZZZ=ZZ.^(1/2.2);            % camera responce function
a=max(max(ZZZ));
figure;
imshow(ZZZ/(a/2))
imwrite(ZZZ/(a/2), 'diffraction_image.png')

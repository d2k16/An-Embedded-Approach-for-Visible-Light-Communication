


H=[162.12,156.24,151.63,147.11,146.00,289.94,390.93,441.15,472.27,494.07.....................];
y=fft(H);
k=abs(y/length(H));
k = k(1:length(H)/2);
Fs=length(H)/3;
fs=Fs*(0:length(H)/2-1)/length(H);
a=find(fs>48 & fs<52);
b=find(fs>69 & fs<73);
c=find(fs>120 & fs<127);

d=find(fs>146 & fs<152);
disp(max(k(a)));
disp(max(k(b)));
disp(max(k(c)));
disp(max(k(d)));

plot(fs,k)

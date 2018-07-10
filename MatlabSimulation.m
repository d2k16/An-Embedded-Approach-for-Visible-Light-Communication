## The Matlab code illustrate the object location estimation based on distance calculation, A simulation model is created and  random point generated in the grid of 100x100 the distances are calculated from the four corner of the grid and a random error is introduced we assumed that the distances are calculated from RSS and an error is in the distance so we estimate the point by applying Trilateration

clc
networkSize=100;
LedAr=100;
LedPos=[0 0;0 100;100 100;100 0];
N=4;
M1=1;
xd=100;
yd=100;
clf
DisEr=zeros(100,1);
for i=1:20
        x=100*rand(1);
        y=100*rand(1);
        %x=50*rand(1);
        %y=50*rand(1);
        mobloc=[x y];
        d1=sqrt(x.^2+y.^2)+15*randn-.5;
        d2=sqrt(x.^2+(y-100).^2)+5*randn-.5;
        d4=sqrt(y.^2+(x-100).^2)+5*rand(1)-.5;
        d3=sqrt((x-100).^2+(y-100).^2)+5*rand(1)-.5;
        d=[d1 d2 d3 d4];
        d12=sqrt(x.^2+y.^2);
        d22=sqrt(x.^2+(y-100).^2);
        d42=sqrt(y.^2+(x-100).^2);
        d32=sqrt((x-100).^2+(y-100).^2);
        %e1=d1-d12;
        %e2=d2-d22;
        %e3=d3-d32;
        %e4=d4-d42;

        %1 and 2 intersection=d1.^2
        y1=(d1.^2+100.^2-d2.^2)/200; %intersection btn 1 & 2
         x1=sqrt(d1.^2-y1.^2);
         L(1)=x1;
         M(1)=y1;
         x2=  (100.^2-d4.^2+d1.^2)/200;     %1&4
         y2=sqrt(d1.^2-x2.^2);
         L(2)=x2;
         M(2)=y2;
         x3=(d1.^2-d4.^2+100^2)/200;
         y3=(d1.^2+100.^2-d2.^2)/200;
         L(3)=x3;
         M(3)=y3;
         X=[mean(L) mean(M)];
         
        u=5.3434;
        Sd=2.7794;
         
         
         %Xsq=[mean(L) mean(M)];
         
         %Xsq=[abs(mean(sqrt(sum(L.^2)))) abs(mean(sqrt(sum(M.^2))))];
         dr=zeros(4,1);
         
         for i=1:4
                dr(i)= sqrt((X(:,1)-LedPos(i,1)).^2+(X(:,2)-LedPos(i,2)).^2);
                
         end
        
        f(1)=figure(1);
         clf
 
         plot(LedPos(:,1),LedPos(:,2),'ko','MarkerSize',8,'lineWidth',2,'MarkerFaceColor','k');
         grid on
         hold on
         plot(x,y,'k+','MarkerSize',8,'lineWidth',2,'MarkerFaceColor','k');

         plot(X(:,1),X(:,2),'ro','MarkerSize',5,'lineWidth',2);
        % plot(Xsq(:,1),Xsq(:,2),'b*','MarkerSize',4,'lineWidth',2);   
                 %plot(Xsq1(:,1),Xsq1(:,2),'mo','MarkerSize',4,'lineWidth',2);   

            legend('LEDs Position','Object true location','Object estimated location',...
                   'Location','Best');
          %plot(X(:,1),X(:,2),'bo','MarkerSize',50,'lineWidth',.1); 
            x=X(:,1);
            y=X(:,2);
            r=9.68;
            
            th = 0:pi/50:2*pi;
            xunit = r * cos(th) + x;
            yunit = r * sin(th) + y;
            plot(xunit, yunit)
            
          
               % Compute the Root Mean Squred Error
            Err = abs(mean(sqrt(sum((X-mobloc).^2))));
            %Err2 = abs(mean(sqrt(sum((Xsq-mobloc).^2))));

            %DisEr=zeros(100,1);
            
            DisEr(i,:)=[Err];
            i=i+1;
            title(['Mean Estimation error is ',num2str(Err),'meter'])

            axis([-0.1 1.1 -0.1 1.1]*networkSize)
%    
    
    
    pause(1);
    
end 

   

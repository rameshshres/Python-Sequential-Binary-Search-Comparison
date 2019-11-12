% Set sample size vector
n = [5000, 6000, 7000, 8000, 9000, 10000];

# Set vectors for the results of each algorithm
exp_time_seq = [0.000566, 0.000666, 0.000792, 0.000882, 0.00104, 0.00116 ];
exp_time_bin=[0.00000751, 0.00000761, 0.00000761, 0.00000751, 0.00000851, 0.00000841];
exp_time_pyth=[0.0000885, 0.000117, 0.000126, 0.000144, 0.000166, 0.000185];

% Estimated theoretical C values based on an average of experimental values.
C_seq = 0.000000113;
C_bin= 0.000000612;
C_pyth=0.0000000183;  

% Theoretical Run Times
theory_seq = C_seq *n;
theory_bin= C_bin*log2(n);
theory_pyth= C_pyth*n;

% Plot all the trends
figure(1)
clf
plot( n, exp_time_seq, 'ro' )

hold on
plot( n, exp_time_bin, 'mo')
plot(n, exp_time_pyth, 'ko')
plot( n, theory_seq, 'y-' )
plot( n, theory_bin, 'g-' )
plot( n, theory_pyth, 'c-' )

hold off

% Make a legend for the trends
legend( ' experimental seq ', 'experimental bin', 'experimental pyth', 
'theory seq', 'theory bin', 'theory pyth', 'Location', 'northwest' )

% Format axes and title
xlabel( ' list length n ' )
ylabel( 'run time f(n) in sec' )
title( 'Search and compare Algorithms  ' )

set( gcf, 'Color', [ 1 1 1 ] )

% Plot all the trends on a loglog plot.
figure(2)
clf
loglog( n, exp_time_seq, 'mo' )      
hold on
loglog( n, exp_time_bin, 'ko' )    
loglog( n, exp_time_pyth, 'ro' )     
loglog( n, theory_seq, 'b-' )
loglog( n, theory_bin, 'k-' )
loglog( n, theory_pyth, 'g-' )
hold off
%set axis label
xlabel('log(n)')
ylabel('log(f(n))')
%set axis title
title('Search and compare Algorithms  log-log Axes')
%set axis legend

legend( ' experimental seq ', 'experimental bin', 'experimental pyth', 
'theory seq', 'theory bin', 'theory pyth' ,'Location', 'southwest')

axis tight


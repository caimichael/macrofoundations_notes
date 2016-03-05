# %  root_finding.m
# %  Calculations for solving f(x) = 0 for x
# %  Example:  f(x) = x^2 - a
# %  Examples of bisection, Newton's method, and the secant method
# %  See Wikipedia ("root-finding") or Atkinson, "Numerical Analysis."
# %  NYU course ECON-UB 233, Macro foundations for asset pricing, Mar 2012.


print('1. Bisection')


a = 8
# this is the number we're trying to find the square root of


# convergence parameters
tol = 0.00000001
maxit = 50

x_low = 0
x_high = a





for i in range(maxit):
    mid = (x_low + x_high)/2
    if (x_low**2-a>0 and mid**2-a>0) or (x_low**2-a<0 and mid**2-a<0):
        x_low = mid
    else:
        x_high = mid
# ahhhh this part took me so long to get


print("answer: " + str((x_low + x_high)/2))
# square root approximation



print("2. Newton's method")























#
# for it in range(1,maxit+1):
#     x_new = (x_lo+x_hi)/2
#     f_new = x_new**2 - a
#     diff_x = abs(x_lo-x_hi)
#     diff_f = abs(f_new)
#     if (diff_x < tol and diff_f < toll):
#         break
#
#
#
#
#
# t0 = cputime;
# for it = 1:maxit
#     x_new = (x_lo+x_hi)/2;      % cut interval in half
#     f_new = x_new.^2 - a;
#     diff_x = max(abs(x_lo-x_hi));
#     diff_f = max(abs(f_new));
#     if max(diff_x,diff_f)<tol, break, it, end
#     if sign(f_new)==sign(f_lo)
#         x_lo = x_new;
#         f_lo = f_new;
#     else
#         x_hi = x_new;
#         f_hi = f_new;
#     end
# end

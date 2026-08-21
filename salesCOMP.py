import numpy as np
months = np.array(["jan","feb","march","april","may","june","july","aug","sep","oct","nov","dec"])
sales = []
print("enther the sales amount in ($1000) fir each month :")
for month in months:
    value = float(input(f"{months}:"))
    sales.append(value)

sales= np.array(sales)
print("COMAPNY SALES ANALYSIS")
print("total sales of the year:",np.sum(sales),"$")
print("average monthly sales:",np.mean(sales),"$")
print("highest sales ever:",np.max(sales),"$")
print("lowest sales ever:",np.min(sales),"$")

best_month  =months[np.argmax(sales)]
worst_month = months[np.argmin(sales)]

print ("best month:",best_month)
print("worst month :",worst_month)

above_average = months[sales > np.mean(sales)]
below_average = months[sales < np.mean(sales)]


print("above avg sales in particular:",above_average)
print("below avg sales in particular:",below_average)

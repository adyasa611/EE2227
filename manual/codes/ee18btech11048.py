import numpy as np 
import matplotlib.pyplot as plt
ht = np.arange(0, 100, 1)             #We define ht from t=0 to 100
xt = np.ones(100)                     #We define input from t=0 to 100 such that it is 1 for all values of t except t=0,1 where its 0
ht[0]=0
ht[1]=0

answer=np.convolve(ht, xt)            # Convolution will give 100+100-1 =199 terms
final = np.zeros(100)
for j in range (100):
	final[j]=answer[j]                # Final stores the value of the first hundred convolution terms since we note time for first 100 units

time=np.arange(0,100,1)
plt.plot(time,final)                  # Plot of convolution vs time
plt.plot(final[0],'ro')
plt.plot(final[1],'ro')
plt.text(1,final[1],'('+str(time[1])+','+str(final[1])+')')
plt.xlabel("Time")
plt.ylabel("y(t)=x(t)*h(t)")     
plt.title("Convolution Output")          
plt.show()

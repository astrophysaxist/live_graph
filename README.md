This pair of scripts showcase the use of matplotlib's *animation.FuncAnimation*
function to plot results from a file that is updating in real time.

The general method is to define an animation function (graph in this example)
to be iteratably evaluated using *FuncAnimation*. The animation function must
contain at least one argument, the frame number, but can also include
other arguments passed to *FuncAnimation* via the *fargs* keyword. The animation
function is evaluated after the interval in ms given to FuncAnimaion via the
*interval* keyword.

To use these example scripts, simply start the *random_live_data* script.

```
python random_live_data.py 15 0.2
```

This script generates a 2 column file of time and 15 second period sine wave
amplitude data with some Gaussian noise (0.2 in scale) called
*test_live_data.dat*. Values are added to this script every 1.0 s as defined by
the dt variable in the script. **OJO This script uses a while loop that
terminates after 100 evaluations.**

In a separate shell or terminal, run the live graph script.

```
python live_graph.py test_live_data.dat 1000
```

This script runs the *FuncAnimation* function and contains the definition of the
animate function--graph. As data is added to the pointed to file in the
script's first commandline arguments, data will be replotted every 1000 ms.

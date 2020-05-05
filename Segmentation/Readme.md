
Needs to be done:

|Task | Description | Assigned | Done?|
|-----|-------------|----------|------|
|3d Segments from 2d Network| Take a 3d img, split it into a stack of 2d images, feed them into the 2d network, recompile them into a 3d image. Code should take a 3d img file as input and output a 3d seg file|Zachary||
|Comparing 3d Segments| Write some code to compare (and possibly visualize) 3d segments using DICE, IOU, Jaccard. Preferably, code should take 2 3d seg files and return a list of comparison statistics, and a 3d visualization with some indication of where the differences are.|Ruobing||
|Metric Eval| Do some experiments trading off between binary cross entropy and dice, ie A*BCE + (1-A)DICE, what is the best value for A? Pick a couple of values, train for 1-2 epochs, compare. Or pick a couple of values train the 10 epoch weights further. |Linhui||
|Weight analysis| Take a look at 3d weights and try to make some analysis of them. In this section, it would be interesting to bump the first set of conv layers up to about 7x7x7 and then look at those weights.|(Sara)-Nate||

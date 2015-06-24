
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

from tkFileDialog import askopenfilename

from matplotlib.figure import Figure

import Tkinter as Tk

import matplotlib.pyplot as plt

from sklearn import tree

import scipy.integrate

part_data = 0

outputArray = np.array([[0, 1], [1, 1], [2, 1], [3, 1], [4, 2], [5, 2], [6, 1], [7, 4], [8, 4], [9, 4], [10, 4], [11, 4], [12, 3], [13, 3], [14, 5], [15, 1]])
print outputArray


def openfile():

    filename = askopenfilename(parent=root)
    global part_data
    part_data = np.loadtxt(filename)

outputAccurany = 0.73
outputDeviation = 0.23


root = Tk.Tk()
root.wm_title("Group 3")

menubar = Tk.Menu(root)
filemenu = Tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Open Data", menu=filemenu)

root.config(menu=menubar)

'''
fig1 = Figure(figsize=(12,7), dpi=100)
outputPlot = fig1.add_subplot(111)
outputPlot.plot(outputArray[:,1], label='Line 2')
outputPlot.set_xlabel('Seconds', size=12)
outputPlot.set_yticks(np.arange(0, 6, 1.0))
outputPlot.set_yticklabels(['Laying', 'Sitting', 'Standing', 'Walking', 'Walking up', 'Walking down'])


fig1 = Figure(figsize=(12,7), dpi=100)
outputPlot = fig1.add_subplot(111)
outputPlot.plot(outputArray[:,1], label='Line 2')

canvas = FigureCanvasTkAgg(fig1, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg( canvas, root )
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
'''
def niklas_analyze():
    
    frequency = 50.0
    window_len = 1
    window_pass = 0.5


    begin = 0
    end = begin+ (window_pass*frequency)
    while(end < part_data.shape[0]): #mean, std, max/min, medium, norm: FEATURE EXTRACTING
        _avg= part_data[begin:end, :].mean(axis=0)
        _std=np.std(part_data[begin:end, :],axis=0)
        _min=part_data[begin:end, :].min(axis=0)
        _max=np.max(part_data[begin:end, :],axis=0)
        _medium=np.median(part_data[begin:end, :], axis=0)
        _norm=np.linalg.norm(part_data[begin:end, :], axis=0)
        if(begin==0):
            mean=_avg
            std=_std
            minimun=_min
            maximum=_max
            medium=_medium
            norm=_norm
        else:
            mean=np.vstack((mean,_avg))
            std=np.vstack((std,_std))
            minimum=np.vstack((minimun,_min))
            maximum=np.vstack((maximum,_max))
            medium=np.vstack((medium,_medium))
            norm=np.vstack((norm,_norm))
            begin=end
            end=end = begin+ (window_pass*frequency)

  
    
        begin=end
        end=end = begin+ (window_pass*frequency)
        
    '''
    Here should be the brifge between mean and maschine learning!!!
    '''    
 
    data_mean = np.load('/home/niklas/Projects/WebValley/Data/py-workspace/data_mean.npy')
    data_var = np.load('/home/niklas/Projects/WebValley/Data/py-workspace/data_var.npy')

    nClass = len(data_mean)

    labels = []
    nFeatures = []

    for i in range(nClass):
    
        # labels for the different activities    
        # labels.append(np.ones((len(data_mean[i]),1)) * (i+1))
    
        nFeatures.append(len(data_mean[i]))
    
        # end for i

    N = min(nFeatures)

    nTrain = N / 5

    data_rnd = []
    dataTrain = [0, 0, 0, 0, 0, 0]
    labelsTrain = [0]
    dataTest = [0, 0, 0, 0, 0, 0]
    labelsTest = [0]

    for i in range(nClass):
    
        idx = np.arange(N)
        np.random.seed(13)
        np.random.shuffle(idx)

        tmp = np.hstack([data_mean[i][0:N,:], data_var[i][0:N,:]])
        data_rnd.append(tmp[idx])

        labels.append(np.ones((N)) * (i+1))

        dataTrain = np.vstack([dataTrain, data_rnd[i][0:nTrain,:]])
        #labelsTrain = np.vstack([labelsTrain, labels[i][0:nTrain]])
        labelsTrain = np.append(labelsTrain, labels[i][0:nTrain])
    
        dataTest = np.vstack([dataTest, data_rnd[i][nTrain+1:-1,:]])
        #labelsTest = np.vstack([labelsTest, labels[i][nTrain+1:-1]])
        labelsTest = np.append(labelsTest, labels[i][nTrain+1:-1])
    
    # end for i

    dataTrain = dataTrain[1:-1,:]
    labelsTrain = labelsTrain[1:-1]
    dataTest = dataTest[1:-1,:]
    labelsTest = labelsTest[1:-1]

    clf = tree.DecisionTreeClassifier()

    # Train
    clf = clf.fit(dataTrain, labelsTrain)

    labelsPredict = clf.predict(dataTest)

    score = clf.score(dataTest, labelsTest)

    print 'Classification Accuracy %f' % score
    outputLabel.set("Accurancy: %0.2f" % score)
            
    fig1 = Figure(figsize=(12,6), dpi=100)
    outputPlot = fig1.add_subplot(111)
    outputPlot.clear()
    outputPlot.plot(range(len(labelsPredict)), labelsPredict)
    outputPlot.set_xlabel('Seconds', size=12)
    outputPlot.set_yticks(np.arange(0, 6, 1.0))
    outputPlot.set_yticklabels(['Laying', 'Sitting', 'Standing', 'Walking', 'Walking up', 'Walking down'])
       
    canvas = FigureCanvasTkAgg(fig1, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    toolbar = NavigationToolbar2TkAgg( canvas, root )
    toolbar.update()
    canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)    
    

button = Tk.Button(master=root, text='Analyze!', command=niklas_analyze)
button.pack(side=Tk.BOTTOM)

outputLabel = Tk.StringVar()
Tk.Label(root, textvariable=outputLabel, font=("Helvetica", 12)).pack()

outputLabel.set("Accurancy: %0.2f (+/- %0.2f)" % (outputAccurany, outputDeviation*2))

Tk.mainloop()



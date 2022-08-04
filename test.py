if self.canvas:
    self.hLayoutMap.removeWidget(self.canvas)
    sip.delete(self.canvas)
    plt.cla
    plt.clf()
    plt.close(self.canvas)

aps = [mpf.make_addplot(somedata, kwargs, ...),
       mpf.make_addplot(otherdata, kwargs, ...), ]
fig, axlist = mpf.plot(self.df, returnfig=True, addplot=aps, volume=True)
canvas = FigureCanvasQTAgg(fig)
self.hLayoutMap.addWidget(canvas)

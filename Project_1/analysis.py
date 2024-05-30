'''analysis.py
Run statistical analyses and plot Numpy ndarray data
YOUR NAME HERE
CS 251/2: Data Analysis and Visualization
Spring 2024
'''
import numpy as np
import matplotlib.pyplot as plt


class Analysis:
    def __init__(self, data):
        '''

        Parameters:
        -----------
        data: Data object. Contains all data samples and variables in a dataset.
        '''
        self.data = data

        # Make plot font sizes legible
        plt.rcParams.update({'font.size': 18})

    def set_data(self, data):
        '''Method that re-assigns the instance variable `data` with the parameter.
        Convenience method to change the data used in an analysis without having to create a new Analysis object.

        Parameters:
        -----------
        data: Data object. Contains all data samples and variables in a dataset.
        '''
        
        self.data = data
        
        return self.data 

    def min(self, headers, rows=[]):
        '''Computes the minimum of each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.
        (i.e. the minimum value in each of the selected columns)

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of min over, or over all indices if rows=[]

        Returns
        -----------
        mins: ndarray. shape=(len(headers),)
            Minimum values for each of the selected header variables

        NOTE: There should be no loops in this method!
        '''
        header_indexes = self.data.get_header_indices(headers)
        
        selected_data = self.data.select_data(headers, rows)
        
        mins = np.min(selected_data, axis= 0)
        
        return mins

    def max(self, headers, rows=[]):
        '''Computes the maximum of each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of max over, or over all indices if rows=[]

        Returns
        -----------
        maxs: ndarray. shape=(len(headers),)
            Maximum values for each of the selected header variables

        NOTE: There should be no loops in this method!
        '''
        header_indexes = self.data.get_header_indices(headers)
        
        selected_data = self.data.select_data(headers, rows)
        
        maxs = np.max(selected_data, axis= 0)
        
        return maxs

    def range(self, headers, rows=[]):
        '''Computes the range [min, max] for each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of min/max over, or over all indices if rows=[]

        Returns
        -----------
        mins: ndarray. shape=(len(headers),)
            Minimum values for each of the selected header variables
        maxes: ndarray. shape=(len(headers),)
            Maximum values for each of the selected header variables

        NOTE: There should be no loops in this method!
        '''
        
        header_indexes = self.data.get_header_indices(headers)
        
        selected_data = self.data.select_data(headers, rows)
        
        mins = np.min(selected_data, axis= 0)
        maxes = np.max(selected_data, axis= 0)
        
        return mins, maxes
        

    def mean(self, headers, rows=[]):
        '''Computes the mean for each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`).

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of mean over, or over all indices if rows=[]

        Returns
        -----------
        means: ndarray. shape=(len(headers),)
            Mean values for each of the selected header variables

        NOTE: You CANNOT use np.mean here!
        NOTE: There should be no loops in this method!
        '''
        
        selected_data = self.data.select_data(headers, rows)
        
        means = np.sum(selected_data, axis= 0) / selected_data.shape[0]
        
        return means 
        

    def var(self, headers, rows=[]):
        '''Computes the variance for each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of variance over, or over all indices if rows=[]

        Returns
        -----------
        vars: ndarray. shape=(len(headers),)
            Variance values for each of the selected header variables

        NOTE:
        - You CANNOT use np.var or np.mean here!
        - There should be no loops in this method!
        '''
        selected_data = self.data.select_data(headers, rows)
        # print(selected_data)
        means = self.mean(headers, rows)
        
        diff = (selected_data - means)**2

        vars = np.sum(diff, axis= 0) / selected_data.shape[0]
        
        return vars

    def std(self, headers, rows=[]):
        '''Computes the standard deviation for each variable in `headers` in the data object.
        Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        Parameters:
        -----------
        headers: Python list of str.
            One str per header variable name in data
        rows: Python list of int.
            Indices of data samples to restrict computation of standard deviation over, or over all indices if rows=[]

        Returns
        -----------
        vars: ndarray. shape=(len(headers),)
            Standard deviation values for each of the selected header variables

        NOTE:
        - You CANNOT use np.var, np.std, or np.mean here!
        - There should be no loops in this method!
        '''
                
        vars = self.var(headers, rows)
         
        stds = np.sqrt(vars)
        
        return stds

    def show(self):
        '''Simple wrapper function for matplotlib's show function.

        (Does not require modification)
        '''
        plt.show()

    def scatter(self, ind_var, dep_var, title):
        '''Creates a simple scatter plot with "x" variable in the dataset `ind_var` and "y" variable in the dataset
        `dep_var`. Both `ind_var` and `dep_var` should be strings in `self.headers`.

        Parameters:
        -----------
        ind_var: str.
            Name of variable that is plotted along the x axis
        dep_var: str.
            Name of variable that is plotted along the y axis
        title: str.
            Title of the scatter plot

        Returns:
        -----------
        x. ndarray. shape=(num_data_samps,)
            The x values that appear in the scatter plot
        y. ndarray. shape=(num_data_samps,)
            The y values that appear in the scatter plot

        NOTE: Do not call plt.show() here.
        '''
        
        x_data = self.data.select_data([ind_var])
        y_data = self.data.select_data([dep_var])
        
        
        plt.scatter(x_data, y_data)
        
        
        plt.xlabel(ind_var)
        plt.ylabel(dep_var)
        
        
        plt.title(title)
        
        
        
        return (x_data, y_data)
        

    def pair_plot(self, data_vars, fig_sz=(12, 12), title=''):
        '''Create a pair plot: grid of scatter plots showing all combinations of variables in `data_vars` in the
        x and y axes.

        Parameters:
        -----------
        data_vars: Python list of str.
            Variables to place on either the x or y axis of the scatter plots
        fig_sz: tuple of 2 ints.
            The width and height of the figure of subplots. Pass as a paramter to plt.subplots.
        title. str. Title for entire figure (not the individual subplots)

        Returns:
        -----------
        fig. The matplotlib figure.
            1st item returned by plt.subplots
        axes. ndarray of AxesSubplot objects. shape=(len(data_vars), len(data_vars))
            2nd item returned by plt.subplots

        TODO:
        1. Make the len(data_vars) x len(data_vars) grid of scatterplots
        2. The y axis of the FIRST column should be labeled with the appropriate variable being plotted there.
        The x axis of the LAST row should be labeled with the appropriate variable being plotted there.
        3. Only label the axes and ticks on the FIRST column and LAST row. There should be no labels on other plots
        (it looks too cluttered otherwise!).
        4. Do have tick MARKS on all plots (just not the labels).
        5. Because variables may have different ranges, your pair plot should share the y axis within columns and
        share the x axis within rows. To implement this, add
            sharex='col', sharey='row'
        to your plt.subplots call.

        NOTE: For loops are allowed here!
        '''

        fig, axes = plt.subplots(len(data_vars), len(data_vars), figsize=fig_sz, sharex='col', sharey='row')
            
        fig.suptitle(title)
        
        for x, var in enumerate(data_vars):
            for i, var1 in enumerate(data_vars):
                axes1 = axes[x, i]
                
                axes1.scatter(self.data.select_data([var1]), self.data.select_data([var]), marker="o")
                    
                    
                if i == 0:
                    axes1.set_ylabel(var)
                
                if x == len(data_vars) - 1:
                    axes1.set_xlabel(var1)
                    
                    
                if x != len(data_vars) - 1:
                    axes1.set_xticks([0, 2, 4, 6, 8])
                   
                    
                if i != 0:
                    axes1.set_yticks([0, 1, 2])
                    
                
                
        return fig, axes
                
                
                

        

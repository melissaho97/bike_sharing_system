# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:29:29 2019

@author: Melissa
"""

        # Import Data from Transaction Table
        
        # X-Axis Label: Months
# =============================================================================
#         x_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#         
#         # Y-Axis Label: Total Sales Amount per Month
#         connection = connectDB()
#         cursor = connection.cursor()
#         query = '''SELECT Paid_Amount FROM transaction WHERE Updated_At;'''
#         cursor.execute(query)
#         city_list = []
#         for row in cursor.fetchall():
#             city_list.append(row)
#         disconnectDB(connection)
# =============================================================================
        
                
        Data1 = {
        'Time': ['US','CA','GER','UK','FR'],
        'Sales_Amount': [45000,42000,52000,49000,47000]
       }

        # Create Pandas to structure the input data
        df1 = pd.DataFrame(Data1, columns= ['Time', 'Sales_Amount'])
        df1 = df1[['Time', 'Sales_Amount']].groupby('Time').sum()
        
        # Create a figure object
        # Figure params: figsize(width, height), 
        figure1 = plt.Figure(figsize=(6,5), dpi=110, facecolor="b")
        # add_subplot ->> add multiple plots to a figure
        ax1 = figure1.add_subplot(111)
        
        # FigureCanvasTkAgg can then generate a widget for Tkinter to use
        bar1 = FigureCanvasTkAgg(figure1, master)
        bar1.get_tk_widget().pack(fill=tk.BOTH)
        df1.plot(kind='line', legend=True, ax=ax1)
        plt.title(figure1, 'Sales Report')
        
        #Set Action Buttion Frame
        act_button_frame = tk.Frame(self)
        act_button_frame.pack(padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        save_button = tk.Button(act_button_frame, text = "Save", width = styleDict["buttonWidth"], 
                                command = self.saveImg)
        save_button.pack(side = tk.LEFT)
        
        
        
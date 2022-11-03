import numpy as np

class NACA4(object):
    
    def __init__(self, name, npoints, closed_te = True, cosine_pts = True):
        self.name = name
        self.npoints = npoints
        self.closed_te = closed_te
        self.cosine_pts = cosine_pts
        

        
        # decode the name
        self.m = int(name[0])/100
        self.p = int(name[1])/10
        self.t = int(name[2:])/100
        
    def generate(self):
        self.gen_xc_points()
        self.gen_thickness()
        self.gen_camber_line()
        self.gen_camber_line_slopes()
        self.gen_surface()
    
    def gen_xc_points(self):
        if self.cosine_pts:
            # distribute x points closer to nose
            beta = np.linspace(0.0,math.pi,n+1)
            self.xc = 0.5*(1.0 - np.cos(beta))  # cosine based spacing
        else:
            # linear distribution
            self.xc = np.linspace(0.0,1.0,n+1)
            
    def get_xc_points(self):
        return self.xc

    def gen_thickness(self):
        """generate yt array for xc array"""
        a0 = +0.2969
        a1 = -0.1260
        a2 = -0.3516
        a3 = +0.2843
        
        x = self.xc
        if self.closed_te:
            a4 = -0.1036 # For finite thick TE
        else:
            a4 = -0.1015 # For zero thick TE

        self.yt = 5*t*(a0*np.sqrt(x)+((((a4)*x+a3)*x+a2)*x+a1)*x)
    
    def get_thickness(self):
        return self.yt
    
    def gen_camber_line(self):
        if self.p == 0:
            # symmetric airfoil
            self.yc = np.zeros(n)
        else:
            # split the chordwise points at the max thickness point
            x1 = [x for x in self.xc if x <= self.p]
            x2 = [x for x in self.xc if x > self.p]
            yc1 = [self.m/(self.p**2)*x*(2*self.p-x) for x in x1]
            yc2 = [self.m/(1-self.p)**2*(1-2*self.p+x)*(1-x) for x in x2]
            
            # save for later
            self.x1 = x1
            self.x2 = x2
            
            self.yc = np.array(yc1 + yc2)
        
    def get_camber_line(self):
        return self.yc
    
    def gen_camber_line_slopes(self):
        if self.p == 0:
            # symmetric airfoil
            theta = np.zeros(self.npoints)
        else:
            dyc1_dx = [self.m/(self.p**2)*(2*p-2*x) for x in self.x1]
            dyc2_dx = [self.m/(1-self.p)**2*(2*self.p-2*x) for x in self.x2]
            dyc_dx = dyc1_dx + dyc2_dx
            theta = np.arctan(dyc_dx)
        self.theta = theta
            
    def get_camber_line_slopes(self):
        return self.theta
    
    def gen_surface(self):
        self.xu = self.xc - self.yt*np.sin(self.theta)
        self.yu = self.yc + self.yt*np.cos(self.theta)
        self.xl = self.xc + self.yt*np.sin(self.theta)
        self.yl = self.yc - self.yt*np.cos(self.theta)
        
    def get_surface(self):
        return self.xu, self.yu, self.xl, self.yl

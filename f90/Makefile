FC	= gfortran

SRCS	= main.f90 \
		  indata.f90

OBJS = $(SRCS:.f90=.o)

all: airfoil

airfoil:	$(OBJS)
	$(FC) $^ -o $@

%.o:	%.f90
	$(FC) -c $< -o $@


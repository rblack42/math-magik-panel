subroutine indata

  common /bod/ nlower,nupper,nodtot,x(100),y(100),costhe(100),sinthe(100)
  common /par/ naca,tau,epsmax,ptmax

  integer :: FID = 1 
  integer :: naca
  integer :: nupper
  integer :: nlower
  character*20 :: nstr
  character :: equals
  integer :: npoints
  logical :: close_te
  logical :: cosine_pts


  open(unit=FID, file='case1.dat', status='old', action='read')

  read(FID,*) nstr, equals, naca
  read(FID,*) nstr, equals, npoints
  read(FID,*) nstr, equals, close_te
  read(FID,*) nstr, equals, cosine_pts


  nlower = npoints
  nupper = npoints

  write(*,'(A,I5)') 'loaded naca number', naca
 
  ieps=naca/1000
  iptmax=naca/100-10*ieps
  itau=naca-1000*ieps-100*iptmax
  epsmax=ieps*0.01
  ptmax=iptmax*0.1
  tau=itau*0.01
  if (ieps.lt.10) return
  ptmax=0.2025
  epsmax=2.6595*ptmax**3
 
  write(*.'(A,I3)') 'points = ", npoints
  write(*,'(A,L2)') 'close_te = ', close_te
  write(*,'(A,L2)') 'cosine_pts = ', cosine_pts

  return
end


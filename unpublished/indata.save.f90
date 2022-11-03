program indata
implicit none

integer :: FID = 1
integer :: IERR = 0

character*5 :: name
integer :: npoints
logical :: close_te
logical :: cosine_pts

character*100 :: nstr
character*1 :: equals

open(unit=FID, file='case1.dat', status='old', action='read')

read(FID,*) nstr, equals, name
read(FID,*) nstr, equals, npoints
read(FID,*) nstr, equals, close_te
read(FID,*) nstr, equals, cosine_pts

write(*,'(A,A)') "Name: ",trim(name)
write(*,'(A,I4)') "Npoints:", npoints
write(*,'(A,L)') "close_te:", close_te
write(*,'(A,L)') "cosine_pts:", cosine_pts

end program indata


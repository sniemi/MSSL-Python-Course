SUBROUTINE example(sinp, xdim, ydim, sout)

IMPLICIT NONE

!inputs and outputs
INTEGER, INTENT(in)                                  :: xdim, ydim
DOUBLE PRECISION, DIMENSION(xdim, ydim), INTENT(in)  :: sinp
DOUBLE PRECISION, DIMENSION(xdim, ydim), INTENT(out) :: sout
!work variables
INTEGER                                              :: i, j

!simple transpose
DO i = 1, xdim
   DO j = 1, ydim
      sout(j, i) = sinp(i, j)
   ENDDO
ENDDO

END SUBROUTINE example

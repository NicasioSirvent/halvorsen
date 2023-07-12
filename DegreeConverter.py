class DegreeConverter:
  def f2c( self, Tf ):
    return (Tf - 32) * 5/9

  def c2f ( self, Tc ):
    return (Tc * 9/5) + 32

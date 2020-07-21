Equations
====================

Wait, what equations are you solving?

See `<https://documentation.help/Sphinx/math.html>`_ for the latex notation.

Since Pythagoras, we know that :math:`a^2 + b^2 = c^2`.

.. math::

   (a + b)^2 = a^2 + 2ab + b^2

   (a - b)^2 = a^2 - 2ab + b^2

Or

.. math::

   (a + b)^2  &=  (a + b)(a + b) \\
              &=  a^2 + 2ab + b^2


When the math is only one line of text, it can also be given as a directive argument:

.. math:: (a + b)^2 = a^2 + 2ab + b^2

Or

.. math::
   :nowrap:

   \begin{eqnarray}
      y    & = & ax^2 + bx + c \\
      f(x) & = & x^2 + 2xy + y^2
   \end{eqnarray}

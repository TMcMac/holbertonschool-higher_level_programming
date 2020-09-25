#!/ur/bin/python3
""" A function to multiply two matracies """


def matrix_mul(m_a, m_b):
    """
    matrix_mul - a function to multiple two equally sized matracies
    arg1: a matrix of integers or floats
    arg2: a matrix of integers or floats
    return  - a new matrix of the products of m_a * m_b
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if not isinstance (m_b, list):
        raise TypeError('m_b must be a list')
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    for alist in m_a:
        if not isinstance(alist, list):
            raise TypeError('m_a must be a list of lists')
        if len(alist) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
        for num in alist:
            if not isinstance(num, (int, float)):
                raise TypeError('m_a should contain only integers or floats')
    for blist in m_b:
        if not isinstance(blist, list):
            raise TypeError('m_b must be a list of lists')
        if len(blist) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')
        for num in blist:
            if not isinstance(num, (int, float)):
                raise TypeError('m_b should contain only integers or floats')

    m_c = []

    for i in range(len(m_a)):
        res = []
        for j in range(len(m_b[0])):
            result = 0
            for k in range(len(m_b)):
                result += m_a[i][k] * m_b[k][j]
            res.append(result)
        m_c.append(res)

    return(m_c)
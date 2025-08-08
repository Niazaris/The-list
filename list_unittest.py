import pytest
from list import List

@pytest.fixture
def lists():
    m_list = List()
    p_list = []
    
    for i in [5, 76, 69, 333, 69]:
        m_list.append(i)
        p_list.append(i)

    return m_list, p_list

def test_append_and_printing(lists):
    m_list, p_list = lists
    
    for i in ["slaanesh", 456, 33, "tzeebtch"]:
        m_list.append(i)
        p_list.append(i)
        
    assert str(m_list) == str(p_list)
    # make error handling for incorrect inputs

def test_insert(lists):
    m_list, p_list = lists
    
    m_list.insert(3, 15)
    p_list.insert(3, 15)
    assert str(m_list) == str(p_list)
    
    m_list.insert(0, "slaanesh")
    p_list.insert(0, "slaanesh")
    assert str(m_list) == str(p_list)
    
    m_list.insert(-2, "slaanesh")
    p_list.insert(-2, "slaanesh")
    assert str(m_list) == str(p_list)
    
    m_list.insert(150, 66)
    p_list.insert(150, 66)
    assert str(m_list) == str(p_list)
    
    m_list.insert(-150, 99)
    p_list.insert(-150, 99)
    assert str(m_list) == str(p_list)
    
    with pytest.raises(TypeError):
        m_list.insert("a", 5)
    with pytest.raises(TypeError):
        p_list.insert("a", 5)
        
def test_remove(lists):
    m_list, p_list = lists
    
    m_list.remove(69)
    p_list.remove(69)
    assert str(m_list) == str(p_list)

    m_list.append('slaanesh')
    p_list.append('slaanesh')
    
    m_list.remove('slaanesh')
    p_list.remove('slaanesh')
    assert str(m_list) == str(p_list)
    
    with pytest.raises(ValueError):
        m_list.remove(9999)
    with pytest.raises(ValueError):
        m_list.remove(9999)
    
def test_clear(lists):
    m_list, p_list = lists
    
    m_list.clear()
    p_list.clear()
    
    assert str(m_list) == str(p_list)
    
def test_pop(lists):
    m_list, p_list = lists
    
    assert m_list.pop(2) == p_list.pop(2)   
    assert str(m_list) == str(p_list)
    
    with pytest.raises(TypeError):
        m_list.pop("a")
    with pytest.raises(TypeError):
        p_list.pop("a")
        
    with pytest.raises(IndexError):
        m_list.pop(999)
    with pytest.raises(IndexError):
        p_list.pop(999)
        
    m_list.clear()
    p_list.clear()
    
    with pytest.raises(IndexError):
        m_list.pop(1)
    with pytest.raises(IndexError):
        p_list.pop(1)
    
def test_reverse(lists):
    m_list, p_list = lists
    
    assert str(m_list.reverse()) == str(p_list.reverse())
    
def test_extend(lists):
    m_list, p_list = lists
    e_list = [567, 3, 22, "slaanesh", 88, 554]
    
    m_list.extend(e_list)
    p_list.extend(e_list)
    
    assert str(m_list) == str(p_list)
    
    with pytest.raises(TypeError):
        m_list.extend(55)
    with pytest.raises(TypeError):
        p_list.extend(55)
    
def test_index(lists):
    m_list, p_list = lists
  
    extension = [64, 333, 69, 31, 7, "slaanesh", 3987, 69]  
    m_list.extend(extension)
    p_list.extend(extension)
    
    assert m_list.index(69) == p_list.index(69)
    assert m_list.index("slaanesh") == p_list.index("slaanesh")
    assert m_list.index(69, 5) == p_list.index(69, 5)
    assert m_list.index(69, 2, 7) == p_list.index(69, 2, 7)
    assert m_list.index(69, 3, -1) == p_list.index(69, 3, -1)
    assert m_list.index(69, -6, -1) == p_list.index(69, -6, -1)
    assert m_list.index(69, 1, 99) == p_list.index(69, 1, 99)
    
    with pytest.raises(ValueError):
        m_list.index(69, 99, -1)        
    with pytest.raises(ValueError):
        m_list.index(69, 99, -1)
        
    with pytest.raises(TypeError):
        m_list.index(69, "a", 6)
    with pytest.raises(TypeError):
        p_list.index(69, "a", 6)
        
    with pytest.raises(TypeError):
        m_list.index(69, 1, "a")
    with pytest.raises(TypeError):
        p_list.index(69, 1, "a")
    
def test_count(lists):
    m_list, p_list = lists
    
    assert m_list.count(69) == p_list.count(69)
    
def test_len(lists):
    m_list, p_list = lists
    
    assert len(m_list) == len(p_list)

def test_copy(lists):
    m_list, p_list = lists
    
    new_m_list = m_list.copy()
    new_p_list = p_list.copy()
    
    assert str(new_m_list) == str(new_p_list)
    
def test_get(lists):
    m_list, p_list = lists
    
    assert str(m_list[2]) == str(p_list[2])
    
    assert str(m_list[2::]) == str(p_list[2::])
    assert str(m_list[1:4:]) == str(p_list[1:4:])
    assert str(m_list[1:5:2]) == str(p_list[1:5:2])
    assert str(m_list[-5:-1:]) == str(p_list[-5:-1:])
    # assert str(m_list[1:8:-1]) == str(p_list[1:8:-1])
    
    with pytest.raises(IndexError):
        m_list[100]
    with pytest.raises(IndexError):
        p_list[100]
    
    with pytest.raises(ValueError):
        m_list[::0]
    with pytest.raises(ValueError):
        p_list[::0]
        

    
if __name__ == '__main__':
    pytest.main()
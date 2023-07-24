# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
# (Может помочь метод translate из модуля string)
import string
from collections import deque
from typing import List, Tuple, Any

LIMIT = 10
TEXT = "A scope defines the visibility of a name within a block. " \
       "If a local variable is defined in a block, its scope includes that block." \
       " If the definition occurs in a function block, the scope extends to any blocks contained within the" \
       " defining one," \
       " unless a contained block introduces a different binding for the name. When a name is used in a code block," \
       " it is resolved using the nearest enclosing scope. " \
       "The set of all such scopes visible to a code block is called the block’s environment." \
       " When a name is not found at all, a NameError exception is raised. If the current scope is a function scope," \
       " and the name refers to a local variable that has not yet been bound to a value at the point where the name" \
       " is used," \
       " an UnboundLocalError exception is raised. UnboundLocalError is a subclass of NameError." \
       " If a name binding operation occurs anywhere within a code block," \
       " all uses of the name within the block are treated as references to the current block." \
       " This can lead to errors when a name is used within a block before it is bound." \
       " This rule is subtle. Python lacks declarations and allows name binding operations to occur anywhere within" \
       " a code block." \
       " The local variables of a code block can be determined by scanning the entire text of the block for name " \
       "binding operations." \
       " See the FAQ entry on UnboundLocalError for examples. " \
       "If the global statement occurs within a block, all uses of the names specified in the statement refer to the " \
       "bindings of those names in the top-level namespace. Names are resolved in the top-level" \
       " namespace by searching the global namespace, i.e. the namespace of the module containing the code block," \
       " and the builtins namespace, the namespace of the module builtins. The global namespace is searched first. " \
       "If the names are not found there, the builtins namespace is searched. " \
       "The global statement must precede all uses of the listed names. " \
       "The global statement has the same scope as a name binding operation in the same block." \
       " If the nearest enclosing scope for a free variable contains a global statement," \
       " the free variable is treated as a global. The nonlocal statement causes corresponding names to refer" \
       " to previously bound variables in the nearest enclosing function scope." \
       " SyntaxError is raised at compile time if the given name does not exist in any enclosing function scope."


def normalize_string(st: str) -> list:
    temp = str.maketrans("", "", string.punctuation)
    result = st.translate(temp)
    result = result.split()
    return result


def count_words(lst: list) -> dict:
    d = dict()
    for i in lst:
        d[i] = lst.count(i)
    return d


def sort_dict(d: dict) -> list[tuple[Any, Any]]:
    sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict


result = set()
normalize_list = normalize_string(TEXT)
interim_result = count_words(normalize_list)
# print(interim_result)
interim_result = sort_dict(interim_result)
# print(interim_result)
for elem in interim_result:
    if LIMIT != 0:
        LIMIT -= 1
        result.add(elem)
print(result)

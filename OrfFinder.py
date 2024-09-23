"""

Author: Amanda Teh 
ORFfinder
"""
# ==========
# Q1

class TrieNode:

    def __init__(self):
        """
        Initialize a TrieNode with an array of children (one for each character 'A', 'B', 'C', 'D')
        and a list to store the indices where each prefix occurs.

        Postcondition: A TrieNode is created with an empty children array and an empty indices list.

        Output: A new TrieNode object.

        Time complexity: Best and worst case is O(1) because initializing is done in constant time.

        Space complexity: O(1) as space needed is constant.
        """

        self.children = [None] * 4  # 'A', 'B', 'C', 'D'
        self.indices = []

    def get_child_index(self, char):
        """
        To get the index in the children array corresponding to the given character.

        Precondition: Char is of 'A', 'B', 'C', 'D'
        Postcondition: Returns the index corresponding to the character.

        Input: char (str): A character 'A', 'B', 'C', or 'D'
        Output: int: The index corresponding to the character 

        Time complexity: Best and worst case is O(1) because it involves an arithmetic operation which is in constant time.
        
        Space complexity: 
        O(1) because the space required is constant as only one integer is involved.
        Input space analysis: O(1)
        Aux space analysis: O(1)
        """

        return ord(char) - ord('A')


class Trie:
    def __init__(self):
        """
        This function initializes the Trie with an empty root

        Postcondition: A Trie is created with an empty root TrieNode.

        Output: A new Trie object.

        Time complexity: O(1) because initializing the root node is done in constant time.

        Space complexity:
        The space required for the root node is constant.
        Input space analysis: O(1)
        Aux space analysis: O(1)
        """

        self.root = TrieNode()

    def insert(self, word, index):
        """
        This function inserts a word into the trie along with the starting index of the word in the genome.

        Precondition:
        - word is a string containing 'A', 'B', 'C', or 'D'.
        - index is a valid starting index 

        Postcondition: Word is inserted into the trie with the starting index.

        Input: word, index

        Time complexity: Best and worst case is O(L), where L is the length of the word.
        The function traverses or creates nodes for each character in the word.
        
        Space complexity: 
        Input space analysis: O(L)
        Aux space analysis: O(L)
        As the space required is proportional to the length of the word being inserted.
        """
        node = self.root
        for char in word:
            child_index = node.get_child_index(char)
            if node.children[child_index] is None:
                node.children[child_index] = TrieNode()
            node = node.children[child_index]
            node.indices.append(index)

    def search_prefix(self, prefix):
        """
        This function will search for a prefix in the trie and return all starting indices of words with this prefix.

        Precondition: prefix is a string containing only 'A', 'B', 'C', 'D'

        Postcondition: Returns a list of starting indices of words that have the given prefix.

        Input: prefix to be searched in the trie
        Output: list of starting indices of words that have the given prefix.

        Time complexity: Best and worst case is O(P), where P is the length of the prefix. 
        The function traverses the nodes corresponding to each character in the prefix.

        Space complexity:
        Input space analysis: O(P), where P is the length of the prefix.
        Aux space analysis: O(1)
        The space required for the traversal is proportional to the length of the prefix.
        """
        node = self.root
        for char in prefix:
            child_index = node.get_child_index(char)
            if node.children[child_index] is None:
                return []
            node = node.children[child_index]
        return node.indices

class OrfFinder:
    """
    Class OrfFinder 
    """
    def __init__(self, genome):
        """
        This function initializes the OrfFinder with the provided genome sequence.
        Written by Amanda Teh 

        Precondition: The genome is a string consisting only of characters 'A', 'B', 'C', and 'D'.
        Postcondition: All suffixes of the genome are inserted into the trie.

        Input: genome: A string representing the genome, consisting only of characters 'A', 'B', 'C', and 'D'.
        Output: A new OrfFinder object.

        Time complexity: 
        Inserting all suffixes into the trie involves creating a suffix for each starting index, 
        and each insertion takes linear time relative to the suffix length. 
            Best case analysis: O(N^2), where N is the length of the genome.
            Worst case analysis: O(N^2), where N is the length of the genome.

        Space complexity: 
        The space required for storing all suffixes in the trie is quadratic in the length of the genome.
            Input space analysis: O(N), where N is the length of the genome.
            Aux space analysis: O(N^2), where N is the length of the genome.
        """
        self.genome = genome    
        self.trie = Trie()
        for i in range(len(genome)):
            self.insert_suffix(i)

    def insert_suffix(self, start_index):
        """
        Insert the suffix of the genome starting at start_index into the trie.

        Precondition: start_index is a valid index in the genome.

        Postcondition: The suffix starting at start_index is inserted into the trie.

        Input: start_index 
        Output: none 

        Time complexity:
            Best case analysis: O(N), where N is the length of the genome.
            Worst case analysis: O(N), where N is the length of the genome.

        Space complexity:
        The space required for the insertion is proportional to the length of the suffix.
            Input space analysis: O(1)
            Aux space analysis: O(N), where N is the length of the genome
        """

        node = self.trie.root
        for i in range(start_index, len(self.genome)):
            char = self.genome[i]
            child_index = node.get_child_index(char)
            if node.children[child_index] is None:
                node.children[child_index] = TrieNode()
            node = node.children[child_index]
            node.indices.append(start_index)

    def find(self, start, end):
        """
        Find all substrings in the genome that start with 'start' and end with 'end'.

        Precondition: start and end are strings containing only 'A', 'B', 'C', 'D'.
        Postcondition: Returns a list of substrings that start with 'start' and end with 'end'

        Parameters:
        start (str): The prefix string.
        end (str): The suffix string.

        Returns:
        list: A list of substrings that start with 'start' and end with 'end', sorted lexicographically.

        Time complexity:
        The search for start indices takes O(T) time. 
        For each start index, finding end indices takes O(U) time. 
        Collecting and sorting substrings takes O(V) time.

        Best case analysis: O(T + U + V), where T is the length of the start string,
                            U is the length of the end string, and V is the total length of the output substrings.
        Worst case analysis: O(T + U + V), where T is the length of the start string,
                            U is the length of the end string, and V is the total length of the output substrings.

        Space complexity:
        The space required for the substrings is proportional to the length of the substrings collected.
            Input space analysis: O(T + U), where T is the length of the start string and U is the length of the end string.
            Aux space analysis: O(V), where V is the total length of the output substrings.
        """
        results = []
        start_indices = self.trie.search_prefix(start)
        start_len = len(start)
        end_len = len(end)

        for start_index in start_indices:
            search_start = start_index + start_len
            end_index = self.genome.find(end, search_start)
            while end_index != -1:
                if end_index >= search_start:  # Ensure no overlap
                    substring = self.genome[start_index:end_index + end_len]
                    results.append(substring)
                end_index = self.genome.find(end, end_index + 1)

        # Ensuring results are in lexicographical order
        results.sort()
        return results
    
 
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        # Build graph and indegere
        for recipe, ing_list in zip(recipes, ingredients):
            for ing in ing_list:
                graph[ing].append(recipe)
            indegree[recipe] = len(ing_list)

        # Initialise queue with initial supplies
        queue = deque(supplies)
        result = []

        # BFS traversal
        while queue:
            item = queue.popleft()
            for recipe in graph[item]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    result.append(recipe)
                    queue.append(recipe)

        return result 

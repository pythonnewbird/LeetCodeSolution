while (p.val - root.val) * (q.val - root.val) > 0:
            root = [root.left, root.right][p.val > root.val]
        return root
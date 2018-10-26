import bisect
class ExamRoom1(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.N = N
        self.student = []

    def seat(self):
        """
        :rtype: int
        """
        if not self.student:
            bisect.insort(self.student, 0)
            return 0
        interval, front, back = self.student[0] + 1, -1, self.student[0]
        for i in range(1, len(self.student)):
            cur = self.student[i] - self.student[i - 1]
            if cur > interval:
                if not(cur - interval == 1 and cur % 2 == 1):
                    interval, front, back = cur, self.student[i - 1], self.student[i]
        if front == -1:
            sit = 0
            m = back
        else:
            sit = front + interval // 2
            m = min(sit - front, back - sit)
        if not self.student[-1] == self.N - 1:
            cur = self.N - 1 - self.student[-1]
            if cur > m:
                sit = self.N - 1
        
        if sit == -1:
            return None
        bisect.insort(self.student, sit)
        return sit

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        self.student.remove(p)
        
class ExamRoom(object):
    def __init__(self, N):
        self.N = N
        self.students = []

    def seat(self):
        # Let's determine student, the position of the next
        # student to sit down.
        if not self.students:
            student = 0
        else:
            # Tenatively, dist is the distance to the closest student,
            # which is achieved by sitting in the position 'student'.
            # We start by considering the left-most seat.
            dist, student = self.students[0], 0
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i-1]
                    # For each pair of adjacent students in positions (prev, s),
                    # d is the distance to the closest student;
                    # achieved at position prev + d.
                    d = (s - prev) / 2
                    if d > dist:
                        dist, student = d, prev + d

            # Considering the right-most seat.
            d = self.N - 1 - self.students[-1]
            if d > dist:
                student = self.N - 1

        # Add the student to our sorted list of positions.
        bisect.insort(self.students, student)
        return student

    def leave(self, p):
        self.students.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)

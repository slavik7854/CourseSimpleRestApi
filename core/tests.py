from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from core.models import Student, Course


class CourseListAPIViewTestCase(APITestCase):
    def setUp(self):
        self.student1 = Student.objects.create(
            first_name='first_name1', last_name='last_name1', age='25', phone_number='000000000'
        )
        self.student2 = Student.objects.create(
            first_name='first_name2', last_name='last_name2', age='30', phone_number='111111111'
        )
        self.course = Course.objects.create(
            title='title', description='description', category='category'
        )

        self.url = reverse("course-list")
        self.course_url = reverse(
            "course-detail", kwargs={
                "pk": self.course.pk})

    def test_add_student_to_course(self):
        client = APIClient()
        request = client.get(self.course_url)
        d = request.data
        d['members'] = [self.student1.id]

        request = client.put(self.course_url, d, format='json')

        assert request.status_code == 200
        assert len(request.data['members']) == 1

    def test_remove_student_to_course(self):
        client = APIClient()
        request = client.get(self.course_url)
        d = request.data
        d['members'] = [self.student1.id, self.student2.id]
        request = client.put(self.course_url, d, format='json')

        d = request.data
        d['members'] = []
        request = client.put(self.course_url, d, format='json')

        assert request.status_code == 200
        assert len(request.data['members']) == 0

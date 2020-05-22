from rest_framework import serializers
from core.models import Student, Course, Membership


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    members = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())
    members_data = serializers.SerializerMethodField('get_members_data', read_only=True)

    def get_members_data(self, instance):
        data = Membership.objects \
            .filter(course_id=instance.id) \
            .order_by('student__last_name', 'student__first_name', 'date_joined')
        data = [s.student for s in data]
        return StudentSerializer(data, many=True, context=self.context).data

    class Meta:
        model = Course
        fields = '__all__'

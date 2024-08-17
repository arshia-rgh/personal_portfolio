class BaseModelTestCase:
    model = None
    # should contain only non default fields
    fields = {}
    fields_2 = {}

    def test_create_instance(self):
        instance = self.model._default_manager.create(**self.fields)
        self.assertIsNotNone(instance.pk)

    def test_ordering(self):
        instance1 = self.model._default_manager.create(**self.fields)
        instance2 = self.model._default_manager.create(**self.fields_2)
        instances = self.model._default_manager.all()

        self.assertEqual(list(instances), [instance2, instance1])

    def test_str_representation(self):
        instance = self.model(**self.fields)
        self.assertEqual(str(instance), instance.name)

# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Milestone.modified_at'
        db.add_column(u'django_project_milestone', 'modified_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True, null=True))


    def backwards(self, orm):
        # Deleting field 'Milestone.modified_at'
        db.delete_column(u'django_project_milestone', 'modified_at')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'django_project.comment': {
            'Meta': {'ordering': "('-submit_date',)", 'object_name': 'Comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comment_comments'", 'to': u"orm['auth.User']"}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '3000'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'content_type_set_for_comment'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_pk': ('django.db.models.fields.TextField', [], {}),
            'submit_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'django_project.component': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('project', 'name'),)", 'object_name': 'Component'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_project.Project']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': "('project',)", 'max_length': '64', 'populate_from': "'name'"})
        },
        u'django_project.membership': {
            'Meta': {'unique_together': "(('project', 'member'),)", 'object_name': 'Membership'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joined_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_project.Project']"})
        },
        u'django_project.milestone': {
            'Meta': {'ordering': "('created_at',)", 'unique_together': "(('project', 'name'),)", 'object_name': 'Milestone'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_completed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'deadline': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2016, 3, 13, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_project.Project']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': "('project',)", 'max_length': '64', 'populate_from': "'name'"})
        },
        u'django_project.objecttask': {
            'Meta': {'object_name': 'ObjectTask'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'content_type_set_for_objecttask'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_pk': ('django.db.models.fields.TextField', [], {}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'objecttask_tasks'", 'to': u"orm['django_project.Task']"})
        },
        u'django_project.priority': {
            'Meta': {'unique_together': "(('project', 'name'),)", 'object_name': 'Priority'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_project.Project']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': "('project',)", 'max_length': '64', 'populate_from': "'name'"})
        },
        u'django_project.project': {
            'Meta': {'object_name': 'Project'},
            u'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_projects'", 'to': u"orm['auth.User']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'through': u"orm['django_project.Membership']", 'symmetrical': 'False'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': "('author',)", 'max_length': '128', 'populate_from': "'name'"})
        },
        u'django_project.status': {
            'Meta': {'ordering': "['order']", 'unique_together': "(('project', 'name'),)", 'object_name': 'Status'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'destinations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['django_project.Status']", 'null': 'True', 'through': u"orm['django_project.Transition']", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_initial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_resolved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_project.Project']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': "('project',)", 'max_length': '64', 'populate_from': "'name'"})
        },
        u'django_project.task': {
            'Meta': {'object_name': 'Task'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_tasks'", 'blank': 'True', 'to': u"orm['auth.User']"}),
            'component': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['django_project.Component']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deadline': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'milestone': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['django_project.Milestone']", 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_tasks'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'priority': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['django_project.Priority']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_project.Project']"}),
            'status': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['django_project.Status']"}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'type': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['django_project.TaskType']"})
        },
        u'django_project.tasktype': {
            'Meta': {'unique_together': "(('project', 'name'),)", 'object_name': 'TaskType'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_project.Project']"})
        },
        u'django_project.transition': {
            'Meta': {'unique_together': "(('source', 'destination'),)", 'object_name': 'Transition'},
            'destination': ('django_project.models.ChainedForeignKeyTransition', [], {'to': u"orm['django_project.Status']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sources'", 'to': u"orm['django_project.Status']"})
        }
    }

    complete_apps = ['django_project']
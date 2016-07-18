# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-25 12:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aklub', '0022_auto_20160623_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_before', models.CharField(blank=True, max_length=15, verbose_name='Title before name')),
                ('title_after', models.CharField(blank=True, max_length=15, verbose_name='Title after name')),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('unknown', 'Unknown')], max_length=50, verbose_name='Gender')),
                ('addressment', models.CharField(blank=True, max_length=40, verbose_name='Addressment in letter')),
                ('addressment_on_envelope', models.CharField(blank=True, max_length=40, verbose_name='Addressment on envelope')),
                ('language', models.CharField(choices=[('cs', 'Czech'), ('en', 'English')], default='cs', help_text='This is the language which will be used to communicate with this user. The system will send emails in this language and administrators will use this language in phone calls and personal contacts.', max_length=50, verbose_name='Language')),
                ('telephone', models.CharField(blank=True, max_length=30, verbose_name='Telephone')),
                ('street', models.CharField(blank=True, max_length=80, verbose_name='Street and number')),
                ('city', models.CharField(blank=True, max_length=40, verbose_name='City/City part')),
                ('country', models.CharField(blank=True, default='Česká republika', max_length=40, verbose_name='Country')),
                ('zip_code', models.CharField(blank=True, max_length=10, verbose_name='ZIP Code')),
                ('different_correspondence_address', models.BooleanField(default=False, help_text='User has different correspondence address', verbose_name='Different correspondence address')),
                ('other_support', models.TextField(blank=True, help_text='If the user supports us in other ways, please specify here.', max_length=500, verbose_name='Other support')),
                ('public', models.BooleanField(default=True, verbose_name='Publish my name in the list of supporters')),
                ('wished_tax_confirmation', models.BooleanField(default=True, verbose_name='Send tax confirmation')),
                ('wished_welcome_letter', models.BooleanField(default=True, verbose_name='Send welcome letter')),
                ('wished_information', models.BooleanField(default=True, verbose_name='Send regular news via email')),
                ('active', models.BooleanField(default=True, help_text='Is the user active member? Use this field to disable old or temporary users.', verbose_name='Active')),
                ('profile_text', models.TextField(blank=True, help_text='Tell others why you support Auto*Mat', max_length=3000, null=True, verbose_name='What is your reason?')),
                ('profile_picture', stdimage.models.StdImageField(blank=True, help_text='Your profile picture, which others will see.', null=True, upload_to='profile-images', verbose_name='Profile picture')),
                ('club_card_available', models.BooleanField(default=False, help_text='Is he entitled to posses a club card?', verbose_name='Club card available')),
                ('club_card_dispatched', models.BooleanField(default=False, help_text='Did we send him the club card already?', verbose_name='Club card dispatched?')),
                ('other_benefits', models.TextField(blank=True, help_text='Did he receive some other benefits?', max_length=500, verbose_name='Other benefits')),
                ('note', models.TextField(blank=True, max_length=2000, verbose_name='Note for making a boring form more lively')),
                ('campaigns', models.ManyToManyField(blank=True, help_text='Associated campaigns', to='aklub.Campaign')),
                ('recruiter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aklub.Recruiter')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='userincampaign',
            name='campaign',
            field=models.ForeignKey(blank=True, default=None, help_text='Campaign', null=True, on_delete=django.db.models.deletion.CASCADE, to='aklub.Campaign'),
        ),
        migrations.AlterField(
            model_name='terminalcondition',
            name='variable',
            field=models.CharField(blank=True, choices=[('UserInCampaign.active', 'UserInCampaign Aktivní: BooleanField '), ('UserInCampaign.activity_points', 'UserInCampaign Body za aktivitu: IntegerField '), ('UserInCampaign.additional_information', 'UserInCampaign Rozšiřující informace: TextField '), ('UserInCampaign.addressment', 'UserInCampaign Oslovení v dopise: CharField '), ('UserInCampaign.addressment_on_envelope', 'UserInCampaign Oslovení na obálku: CharField '), ('UserInCampaign.campaign', 'UserInCampaign campaign: ForeignKey '), ('UserInCampaign.city', 'UserInCampaign Město/Městská část: CharField '), ('UserInCampaign.club_card_available', 'UserInCampaign Nárok na klubovou kartu: BooleanField '), ('UserInCampaign.club_card_dispatched', 'UserInCampaign Klubová karta odeslána?: BooleanField '), ('UserInCampaign.country', 'UserInCampaign Země: CharField '), ('UserInCampaign.different_correspondence_address', 'UserInCampaign Jiná korespondenční adresa: BooleanField '), ('UserInCampaign.email', 'UserInCampaign Email: CharField '), ('UserInCampaign.exceptional_membership', 'UserInCampaign Výjimečné členství: BooleanField '), ('UserInCampaign.expected_date_of_first_payment', 'UserInCampaign Očekávané datum první platby: DateField '), ('UserInCampaign.expected_regular_payment_date', 'UserInCampaign expected regular payment date: DateField '), ('UserInCampaign.extra_money', 'UserInCampaign extra money: IntegerField '), ('UserInCampaign.field_of_work', 'UserInCampaign Pracovní oblast: CharField '), ('UserInCampaign.firstname', 'UserInCampaign Jméno: CharField '), ('UserInCampaign.id', 'UserInCampaign ID: AutoField '), ('UserInCampaign.knows_us_from', 'UserInCampaign Odkud nás zná?: CharField '), ('UserInCampaign.language', "UserInCampaign Jazyk: CharField ('cs', 'en')"), ('UserInCampaign.last_payment', 'UserInCampaign last payment: DenormDBField '), ('UserInCampaign.no_upgrade', 'UserInCampaign no upgrade: NullBooleanField '), ('UserInCampaign.note', 'UserInCampaign Poznámka pro oživení nudného formuláře: TextField '), ('UserInCampaign.number_of_payments', 'UserInCampaign number of payments: IntegerField '), ('UserInCampaign.old_account', 'UserInCampaign Starý účet: BooleanField '), ('UserInCampaign.other_benefits', 'UserInCampaign Další benefity: TextField '), ('UserInCampaign.other_support', 'UserInCampaign Jiná podpora: TextField '), ('UserInCampaign.payment_total', 'UserInCampaign payment total: FloatField '), ('UserInCampaign.profile_picture', 'UserInCampaign Profilová fotografie: FileField '), ('UserInCampaign.profile_text', 'UserInCampaign A jaký je Tvůj důvod?: TextField '), ('UserInCampaign.public', 'UserInCampaign Zveřejnit mé jméno v seznamu podporovatelů: BooleanField '), ('UserInCampaign.recruiter', 'UserInCampaign recruiter: ForeignKey '), ('UserInCampaign.registered_support', 'UserInCampaign Registrace podpory: DateTimeField '), ('UserInCampaign.regular_amount', 'UserInCampaign Částka pravidelné platby: PositiveIntegerField '), ('UserInCampaign.regular_frequency', "UserInCampaign Frekvence pravidelných plateb: CharField ('monthly', 'quaterly', 'biannually', 'annually')"), ('UserInCampaign.regular_payments', 'UserInCampaign Pravidelné platby: BooleanField '), ('UserInCampaign.sex', "UserInCampaign Pohlaví: CharField ('male', 'female', 'unknown')"), ('UserInCampaign.source', 'UserInCampaign Zdroj: ForeignKey '), ('UserInCampaign.street', 'UserInCampaign Ulice a číslo domu (č.p./č.o.): CharField '), ('UserInCampaign.surname', 'UserInCampaign Příjmení: CharField '), ('UserInCampaign.telephone', 'UserInCampaign Telefon: CharField '), ('UserInCampaign.title_after', 'UserInCampaign Titul za jménem: CharField '), ('UserInCampaign.title_before', 'UserInCampaign Titul před jménem: CharField '), ('UserInCampaign.userprofile', 'UserInCampaign userprofile: ForeignKey '), ('UserInCampaign.variable_symbol', 'UserInCampaign Variabilní symbol: CharField '), ('UserInCampaign.verified', 'UserInCampaign Ověřen: BooleanField '), ('UserInCampaign.verified_by', 'UserInCampaign Ověřil: ForeignKey '), ('UserInCampaign.why_supports', 'UserInCampaign Proč nás podporuje?: TextField '), ('UserInCampaign.wished_information', 'UserInCampaign Zasílat pravidelné informace emailem: BooleanField '), ('UserInCampaign.wished_tax_confirmation', 'UserInCampaign Zaslat daňové potvrzení (na konci roku): BooleanField '), ('UserInCampaign.wished_welcome_letter', 'UserInCampaign Odeslat uvítací dopis s členskou kartou: BooleanField '), ('UserInCampaign.zip_code', 'UserInCampaign PSČ: CharField '), ('UserInCampaign.last_payment.BIC', 'UserInCampaign.last_payment BIC: CharField '), ('UserInCampaign.last_payment.KS', 'UserInCampaign.last_payment KS: CharField '), ('UserInCampaign.last_payment.SS', 'UserInCampaign.last_payment SS: CharField '), ('UserInCampaign.last_payment.VS', 'UserInCampaign.last_payment VS: CharField '), ('UserInCampaign.last_payment.account', 'UserInCampaign.last_payment Account: CharField '), ('UserInCampaign.last_payment.account_name', 'UserInCampaign.last_payment Jméno účtu: CharField '), ('UserInCampaign.last_payment.account_statement', 'UserInCampaign.last_payment account statement: ForeignKey '), ('UserInCampaign.last_payment.amount', 'UserInCampaign.last_payment Částka: PositiveIntegerField '), ('UserInCampaign.last_payment.bank_code', 'UserInCampaign.last_payment Kód banky: CharField '), ('UserInCampaign.last_payment.bank_name', 'UserInCampaign.last_payment Jméno banky: CharField '), ('UserInCampaign.last_payment.currency', 'UserInCampaign.last_payment Currency: CharField '), ('UserInCampaign.last_payment.date', 'UserInCampaign.last_payment Datum platby: DateField '), ('UserInCampaign.last_payment.done_by', 'UserInCampaign.last_payment Provedl: CharField '), ('UserInCampaign.last_payment.id', 'UserInCampaign.last_payment ID: AutoField '), ('UserInCampaign.last_payment.operation_id', 'UserInCampaign.last_payment Operation ID: CharField '), ('UserInCampaign.last_payment.order_id', 'UserInCampaign.last_payment Order ID: CharField '), ('UserInCampaign.last_payment.recipient_message', 'UserInCampaign.last_payment Recipient message: CharField '), ('UserInCampaign.last_payment.specification', 'UserInCampaign.last_payment Specification: CharField '), ('UserInCampaign.last_payment.transfer_note', 'UserInCampaign.last_payment Transfer note: CharField '), ('UserInCampaign.last_payment.transfer_type', 'UserInCampaign.last_payment Transfer type: CharField '), ('UserInCampaign.last_payment.type', "UserInCampaign.last_payment Typ: CharField ('bank-transfer', 'cash', 'expected', 'darujme')"), ('UserInCampaign.last_payment.user', 'UserInCampaign.last_payment user: ForeignKey '), ('UserInCampaign.last_payment.user_identification', 'UserInCampaign.last_payment Identifikace odesílatele: CharField '), ('UserInCampaign.source.direct_dialogue', 'UserInCampaign.source Pochází z Direct dialogu: BooleanField '), ('UserInCampaign.source.id', 'UserInCampaign.source ID: AutoField '), ('UserInCampaign.source.name', 'UserInCampaign.source Jméno: CharField '), ('UserInCampaign.source.slug', 'UserInCampaign.source Identifikátor: SlugField '), ('action', "Akce: CharField ('daily', 'new-user', 'new-payment')")], help_text='Value or variable on left-hand side', max_length=50, null=True, verbose_name='Variable'),
        ),
        migrations.AddField(
            model_name='userincampaign',
            name='userprofile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aklub.UserProfile'),
        ),
    ]

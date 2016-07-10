# -*- coding: utf-8 -*-

__VERSION__ = '0.1.0'

import os
import sys
import json
import urlparse

from packages import click

from utils import get_file
from utils import extract_packages_info

from repositories import Repository


DEFAULT_CONFIG_PATH=os.path.join(os.path.dirname(os.path.abspath(__file__)), '.repositories.json')

@click.group()
@click.option('-c', '--config',
            type=click.File('r'),
            default=DEFAULT_CONFIG_PATH,
            help='the path to configuration file (.repositories.json)')
@click.version_option(__VERSION__)
@click.pass_context
def cli(ctx, config):
    ''' command line interface to Alpine package mirrorer
    '''
    ctx.obj = dict()
    ctx.obj['current_path'] = os.path.dirname(os.path.abspath(__file__))
    try:
        ctx.obj['repositories'] = json.load(config)
    except IOError, err:
        print >> sys.stderr, '[ERROR] Cannot parse the configuration file, %s' % config
        sys.exit(1)


@cli.command()
@click.pass_context
def list(ctx):
    '''show the list of repositories
    '''
    try:
        for repo, details in ctx.obj['repositories'].items():
            click.echo('%s: %s' % (repo, details['url']))
    except IOError, err:
        print >> sys.stderr, '[ERROR] Cannot parse the configuration file, %s' % config
        sys.exit(1)



@cli.command()
@click.argument('repository')
@click.pass_context
def update(ctx, repository):
    ''' update repository(-ies)
    '''
    if repository not in ctx.obj['repositories']:
        print >> sys.stderr, '[ERROR] The repository does not exist, %s' % repository
        sys.exit(1)

    try:
        mirror_path = os.path.realpath(
                        os.path.join(
                                ctx.obj['current_path'],
                                ctx.obj['repositories'][repository]['mirror-path']
                        )
        )
    except KeyError, err:
        print >> sys.stderr, '[ERROR] Incorrect repositories configuration file, repository: %s [%s]' % (repository, err)
        sys.exit(1)

    repo = Repository(repository, mirror_path, **ctx.obj['repositories'][repository])
    repo.update_index()
    for package in repo.update_packages():
        click.echo("[NEW] %s" % package)

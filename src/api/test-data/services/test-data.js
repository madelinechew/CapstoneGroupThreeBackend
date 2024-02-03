'use strict';

/**
 * test-data service
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::test-data.test-data');
